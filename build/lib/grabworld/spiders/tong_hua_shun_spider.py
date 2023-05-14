# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery as pq
from grabworld.items import StockItem, BaseItemLoader
from grabworld.utils.Utils import datetime_lib


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

    def parse(self, response, **kwargs):
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
                , transaction_volume, floating_stock, circulation_market_value, pe_ratio = tr.text().split('\n')
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
            item_loader.add_value('create_time', datetime_lib.now)
            item_loader.add_value('update_time', datetime_lib.now)
            stock_item = item_loader.load_item()
            yield stock_item

    def start_requests(self):
        for page in range(self.current_page, self.total_page):
            next_url = self.start_urls[0].format(page)
            yield scrapy.Request(url=next_url, headers=self.headers, callback=self.parse)
