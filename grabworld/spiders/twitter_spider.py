# -*- coding: utf-8 -*-
import scrapy


class BasicTestsSpider(scrapy.Spider):
    name = "twitter"
    allowed_domains = ["boss.com"]
    start_urls = ["http://boss.com/"]

    def parse(self, response,**kwargs):
        pass


'https://www.zhipin.com/web/common/security-check.html?seed=jBBj2UwPGBV37Pi%2Bhvn5jlB4xRngSvVhweMWhDL8ZRK3Nl%2FbrSnv8tO8D1m1D13OTyd8AhJv869BpeO3xNZ7ug%3D%3D&name=b9a650ab&ts=1683691439536&callbackUrl=%2Fjob_detail%2F3716135deae284521XZ429--FVNY.html%3Fka%3Dcomp_joblist_1_blank%26lid%3D95I0Gl6heHF.search.1%26securityId%3D&srcReferer=https%3A%2F%2Fwww.zhipin.com%2Fgongsir%2Fb2f9cadc2581ffd533R92tm_.html%3Fka%3Dcompany-jobs'
'web/common/security-check.html?seed=jBBj2UwPGBV37Pi%2Bhvn5jlB4xRngSvVhweMWhDL8ZRK3Nl%2FbrSnv8tO8D1m1D13OTyd8AhJv869BpeO3xNZ7ug%3D%3D&name=b9a650ab&ts=1683691439536&callbackUrl=%2Fjob_detail%2F3716135deae284521XZ429--FVNY.html%3Fka%3Dcomp_joblist_1_blank%26lid%3D95I0Gl6heHF.search.1%26securityId%3D&srcReferer=https%3A%2F%2Fwww.zhipin.com%2Fgongsir%2Fb2f9cadc2581ffd533R92tm_.html%3Fka%3Dcompany-jobs'
import requests

headers = {
    'authority': 'www.zhipin.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
    'cache-control': 'max-age=0',
    'referer': 'https://www.zhipin.com/gongsir/b2f9cadc2581ffd533R92tm_.html?ka=company-jobs',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

params = {
    'seed': 'jBBj2UwPGBV37Pi+hvn5jlB4xRngSvVhweMWhDL8ZRK3Nl/brSnv8tO8D1m1D13OTyd8AhJv869BpeO3xNZ7ug==',
    'name': 'b9a650ab',
    'ts': '1683691439536',
    'callbackUrl': '/job_detail/3716135deae284521XZ429--FVNY.html?ka=comp_joblist_1_blank&lid=95I0Gl6heHF.search.1&securityId=',
    'srcReferer': 'https://www.zhipin.com/gongsir/b2f9cadc2581ffd533R92tm_.html?ka=company-jobs',
}

response = requests.get('https://www.zhipin.com/web/common/security-check.html', params=params, headers=headers)
print(response.text.encode('ISO-8859-1'))
