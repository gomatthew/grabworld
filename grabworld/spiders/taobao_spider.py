# -*- coding: utf-8 -*-
import scrapy


class BasicTestsSpider(scrapy.Spider):
    name = "taobao"
    allowed_domains = ["boss.com"]
    start_urls = ["http://boss.com/"]

    def parse(self, response):
        pass
