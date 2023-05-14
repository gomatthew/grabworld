# -*- coding: utf-8 -*-
import logging
import scrapy
from urllib.parse import urlparse
from pyquery import PyQuery as pq
from grabworld.items import StockItem, BaseItemLoader
from grabworld.utils.Utils import datetime_lib, set_proxy_blacklist


class StockSpider(scrapy.Spider):
    name = "tong_hua_shun"
    allowed_domains = ["10jqka.com.cn"]
    current_page = 1
    total_page = 258
    get_page_tag = False
    start_urls = [
        "http://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/{}/ajax/1/"]
    headers = {
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
        'Connection': 'keep-alive',
        'Referer': 'http://q.10jqka.com.cn/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'hexin-v': '',
    }

    custom_settings = {

        "DOWNLOADER_MIDDLEWARES": {
            "grabworld.middlewares.RandomDelayMiddleware": 301,
            'grabworld.middlewares.GrabworldDownloaderMiddleware': 543,
            # 'grabworld.middlewares.RandomUserAgentMiddlware': 200,
            'grabworld.middlewares.RandomProxyMiddleware': 300,
        }
    }

    def parse(self, response, **kwargs):
        try:
            match response.status:
                case 200:
                    doc = pq(response.text)
                    # match self.get_page_tag:
                    #     case False:
                    #         self.total_page = int(doc('.page_info').text().split('/')[-1]) + 1
                    #         self.get_page_tag = True
                    trs = doc('tr').items()
                    trs.__next__()
                    for tr in trs:
                        item_loader = BaseItemLoader(item=StockItem(), response=response)
                        id, code, stock_name, price, rase_fall_percent, rase_fall_price, rase_fall_speed, turn_over, equivalent_ratio, amplitude \
                            , transaction_volume, floating_stock, circulation_market_value, pe_ratio = tr.text().split(
                            '\n')
                        item_loader.add_value('code', code)
                        item_loader.add_value('stock_name', stock_name)
                        item_loader.add_value('price', price)
                        item_loader.add_value('price_date', datetime_lib.today)
                        item_loader.add_value('rase_fall_percent', rase_fall_percent)
                        item_loader.add_value('rase_fall_price', rase_fall_price)
                        item_loader.add_value('rase_fall_speed', rase_fall_speed)
                        item_loader.add_value('turn_over', turn_over)
                        item_loader.add_value('equivalent_ratio', equivalent_ratio)
                        item_loader.add_value('amplitude', amplitude)
                        item_loader.add_value('transaction_volume', transaction_volume)
                        item_loader.add_value('floating_stock', floating_stock)
                        item_loader.add_value('circulation_market_value', circulation_market_value)
                        item_loader.add_value('pe_ratio', pe_ratio)
                        item_loader.add_value('source_page', response.url)
                        item_loader.add_value('create_time', datetime_lib.now)
                        item_loader.add_value('update_time', datetime_lib.now)
                        stock_item = item_loader.load_item()
                        yield stock_item
                case _:
                    # 直接走本机ip
                    url = response.url
                    proxy = response.meta.get('proxy')
                    with open('/Users/majian/workspace/log/grabworld/proxy_fail.log', 'a', encoding='utf-8') as f:
                        f.write(f'{datetime_lib.now}: {url}: {proxy} {response.status}\r\n')
                    domin = urlparse(response.url).netloc
                    set_proxy_blacklist(f"{domin}:blacklist", proxy)
                    logging.error(f'节点1 重新请求{response.url}')
                    yield scrapy.Request(url=response.url, headers=self.headers, callback=self.parse, dont_filter=True,
                                         meta={'retry_': True})
        except BaseException as e:
            logging.error("日志:\r\n"+str(e))
            domin = urlparse(response.url).netloc
            proxy = response.meta.get('proxy')
            set_proxy_blacklist(f"{domin}:blacklist", proxy)
            logging.error(f'节点2 重新请求{response.url}')
            yield scrapy.Request(url=response.url, headers=self.headers, callback=self.parse, meta={'retry_': True}, dont_filter=True)

    def start_requests(self):
        for page in range(self.current_page, self.total_page):
            next_url = self.start_urls[0].format(page)
            yield scrapy.Request(url=next_url, headers=self.headers, callback=self.parse, errback=self.parse_error)

    def parse_error(self, failure):
        url = failure.value.response.url
        proxy = failure.value.response.meta.get('proxy')
        with open('/Users/majian/workspace/log/grabworld/proxy_fail.log', 'a', encoding='utf-8') as f:
            f.write(f'{datetime_lib.now}: {url}: {proxy} {failure.value.response.status}\r\n')
        domin = urlparse(failure.value.response.url).netloc
        set_proxy_blacklist(f"{domin}:blacklist", proxy)
        logging.error(f'节点3 重新请求{url} ')
        yield scrapy.Request(url=url, headers=self.headers, callback=self.parse, errback=self.parse_error, dont_filter=True)
