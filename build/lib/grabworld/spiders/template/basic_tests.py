import scrapy


class BasicTestsSpider(scrapy.Spider):
    name = "basic_tests"
    allowed_domains = ["boss.com"]
    start_urls = ["http://boss.com/"]

    def parse(self, response):
        pass
