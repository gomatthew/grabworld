# -*- coding: utf-8 -*-
import scrapy
import undetected_chromedriver as uc
from fake_useragent import FakeUserAgent


class BasicTestsSpider(scrapy.Spider):

    def __init__(self):
        super(BasicTestsSpider, self).__init__()
        self.fake = FakeUserAgent()
        self.name = "boss"
        self.allowed_domains = ["boss.com"]
        self.start_urls = ["http://boss.com/"]

    def init_driver(self):
        self.driver = uc.Chrome()
        options = uc.ChromeOptions()
        options.add_argument(f'--user-agent={self.fake.random}')
        options.add_argument("--proxy-server=175.178.123.238:8888")

    def start_requests(self):
    # 模拟登陆
        pass


    def parse(self, response, **kwargs):
        pass
from urllib.parse import unquote
# r = 'https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DpvBnasBNnygB7L7_FczoWBhagaKQERqMCF8rcVhXjpWHlERfk7HPhic2-xBXX9XR%26wd%3D%26eqid%3Dacffec0b0024e8c300000002643a2abd&l=%2Fwww.zhipin.com%2F&s=3&g=&friend_source=0&s=3&friend_source=0'
# x='r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DpvBnasBNnygB7L7_FczoWBhagaKQERqMCF8rcVhXjpWHlERfk7HPhic2-xBXX9XR%26wd%3D%26eqid%3Dacffec0b0024e8c300000002643a2abd%26l%3D%2Fwww.zhipin.com%2F%26s%3D3%26g%3D%26friend_source%3D0%26s%3D3%26friend_source%3D0&l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3DJava%26city%3D100010000&s=3&g=&friend_source=0&s=3&friend_source=0'
# z='r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DpvBnasBNnygB7L7_FczoWBhagaKQERqMCF8rcVhXjpWHlERfk7HPhic2-xBXX9XR%26wd%3D%26eqid%3Dacffec0b0024e8c300000002643a2abd%26l%3D%2Fwww.zhipin.com%2F%26s%3D3%26g%3D%26friend_source%3D0%26s%3D3%26friend_source%3D0%26l%3D%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3DJava%26city%3D100010000%26s%3D3%26g%3D%26friend_source%3D0%26s%3D3%26friend_source%3D0&l=%2Fwww.zhipin.com%2F&s=3&g=&friend_source=0&s=3&friend_source=0'
if __name__ == '__main__':
    r = 'https://www.zhipin.com/web/common/security-check.html?seed=UnmjLt5reYwYELEX8rTiLTkwfN93GkhathGagHvjy1I%3D&name=2b21582d&ts=1683636497224&callbackUrl=https%3A%2F%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3DJava%26city%3D101030100'
    print(unquote(r))
#     print(unquote(x))
#     print(unquote(z))
