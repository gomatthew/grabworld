# -*- coding: utf-8 -*-
import logging
import urllib.parse

import scrapy
from pyquery import PyQuery as pq
from grabworld.items import BaseItemLoader, ProxyItem
from grabworld.utils.Utils import datetime_lib
from grabworld.job import job_manager

# job_manager.job_stop()
# job_manager.job_start()


class ProxySpider(scrapy.Spider):
    name = "proxy_bot"
    allowed_domains = ["89ip.cn"]
    start_urls = ["https://www.89ip.cn", ]
    headers = {"Referer": start_urls[0]}

    # def start_requests(self):
    #     # 一般做模拟登陆，反爬
    #     yield scrapy.Request(url=self.start_urls[0], headers=self.headers, callback=self.parse)

    def parse(self, response, **kwargs):
        if response.status not in [200, 201]:
            # 状态码有问题，可以考虑更换代理或重试访问，如果更换代理仍有问题，记录
            # TODO 更换代理
            return
        doc = pq(response.text)
        # 删除列头
        doc('tr:first').remove()
        items = self.parse_detail(response=response, doc=doc)
        for item in items:
            yield item
        next_url = urllib.parse.urljoin(response.url, doc('a.layui-laypage-next').attr('href'))
        headers = {"Referer": response.url}
        if next_url != response.url:
            yield scrapy.Request(url=next_url, headers=headers, callback=self.parse)

    def parse_detail(self, response, doc):
        trs = doc('tr').items()
        items_list = []
        for tr in trs:
            try:
                ip, port, location, _, own_time = tr.text().split('\n')
                item_loader = BaseItemLoader(item=ProxyItem(), response=response)
                item_loader.add_value('ip', ip)  # ip = scrapy.Field()
                item_loader.add_value('port', port)  # port = scrapy.Field()
                item_loader.add_value('location', location)  # location = scrapy.Field()
                # is_useful = judge_proxy_available(f'{ip.strip()}:{port.strip()}')
                item_loader.add_value('proxy_type', 'http')  # proxy_type = scrapy.Field()
                # anonymous_type = scrapy.Field()
                item_loader.add_value('is_useful', 0)
                item_loader.add_value('create_time', datetime_lib.now)
                item_loader.add_value('update_time', datetime_lib.now)
                proxy_item = item_loader.load_item()
                # yield scrapy.Request(url='', meta={'proxy': f'http://{ip}:{port}','item_loader':item_loader},callback=self.parse)
                # yield proxy_item
                items_list.append(proxy_item)
            except:
                logging.error(f'代理信息解析错误: {tr.text()} !!!')
        return items_list
