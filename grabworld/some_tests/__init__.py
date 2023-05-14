# -*- coding: utf-8 -*-
# import logging
# logging.basicConfig(
#     # 1、日志输出位置：1、终端 2、文件
#     # filename='access.log', # 不指定，默认打印到终端
#
#     # 2、日志格式
#     # format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#     format='%(asctime)s - %(levelname)s -%(module)s:  %(message)s',
#
#     # 3、时间格式
#     datefmt='%Y-%m-%d %H:%M:%S %p',
#
#     # 4、日志级别
#     # critical => 50
#     # error => 40
#     # warning => 30
#     # info => 20
#     # debug => 10
#     level=20,
# )
# logger = logging.getLogger()
# # logging.info("test")
# logger.info('test')
# import time
#
#
# def foo():
#     from grabworld.utils.Utils import datetime_lib
#     print(f"{datetime_lib.now}")
#
#
# from grabworld import job_scheduler
# print(job_scheduler.get_jobs())
# job_scheduler.add_job(id='test',func=foo, trigger="interval", seconds=1)
# job_scheduler.start()
# while True:
#     print(job_scheduler.get_jobs())
#     time.sleep(2)
#     res = job_scheduler.remove_job("test")
#     print(res)
# from  fake_useragent import UserAgent
# ua = UserAgent()
# a = ua.random
# print(a)
import time
from urllib import parse
#
# url = parse.urljoin('https://www.89ip.cn/index_1.html', "index_2.html")
# print(url)

# def foo():
#
#     for i in range(10):
#         yield i
#     yield "a"
#
# if __name__ == '__main__':
#     for i_ in foo():
#         print(i_)


# from pyquery import PyQuery as pq
#
# with open('test.html') as f:
#     file = f.read()
# doc = pq(file)
# doc('tr:first').remove()
# trs = doc('tr').items()
# for tr in trs:
#     test = tr.text().split('\n')
#     print(test)


# def foo():
#     yield 1
# if __name__ == '__main__':
#     foo()

import requests
# from fake_useragent import FakeUserAgent
#
# fake = FakeUserAgent()
headers={
            'Accept': 'application/json',
            'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
            'User-Agent':'Mozilla/5.0 (Linux; Android 9.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Mobile Safari/537.36',
            'Referer':'https://www.zhipin.com/',
            'X-Requested-With':"XMLHttpRequest",
            "cookie":"lastCity=101020100; JSESSIONID=""; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1532401467,1532435274,1532511047,1532534098; __c=1532534098; __g=-; __l=l=%2Fwww.zhipin.com%2F&r=; toUrl=https%3A%2F%2Fwww.zhipin.com%2Fc101020100-p100103%2F; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1532581213; __a=4090516.1532500938.1532516360.1532534098.11.3.7.11"
        }
proxies = {
    "http": f"http://175.178.123.238:8888",
    "https": f"http://175.178.123.238:8888",
}
import time
cookies={}
cookies['__zp_stoken__']='1ea4eC0F3X2h7YB8mAwtyWS54RGQ9OyYbblpHczRNXh4RBQx2A3gqeQx3SzBQTj9HfjtlFzkMP3sSMTUVV0YPNXs%2FWnQ0ZGM4BzJiWnNQNWcMXCEzNwJTBDxAaEMtbQkMPAJXbEQGTwNadEU%3D'
params = {'v2':int(time.time()*1000),'scene':'1','query':'Java','city':'101030100','experience':'','payType':'','partTime':'','degree':'','industry':'','scale':'','stage':'','position':'','jobType':'','salary':'','multiBusinessDistrict':'','multiSubway':'','page':'1','pageSize':'30'}
s = requests.session()
res = s.get('https://www.zhipin.com/wapi/zpgeek/search/joblist.json',proxies=proxies,headers=headers,params=params,cookies=cookies)
print(res.cookies)
# print(res.text)
# url = 'https://www.zhipin.com/web/geek/job?query=Python&city=100010000&page=3'
# url = 'https://www.zhipin.com/'
# s = requests.session()
# s.proxies = proxies
# s.headers = headers
# res = s.get(url=url)
# print(res.cookies.items())
# res = s.get(url='https://www.zhipin.com/web/geek/job?query=Java&city=100010000',  headers=headers,
#             proxies=proxies)
# print(res.cookies.items())
# pass



# import undetected_chromedriver as uc
# from fake_useragent import UserAgent
# fake = UserAgent()
# options = uc.ChromeOptions()
# # options.add_argument(f'--user-agent={fake.random}')
# options.add_argument("--proxy-server=175.178.123.238:8888")
# driver = uc.Chrome(options=options)
# desired_capabilities = options.to_capabilities()
# desired_capabilities['proxy'] = {
#     "httpProxy": '111.229.8.95:3128',
#     # "ftpProxy": PROXY,
#     # "sslProxy": PROXY,
#     "noProxy": None,
#     "proxyType": "MANUAL",
#     # "class": "org.openqa.selenium.Proxy",
#     # "autodetect": False
# }

# driver.get('https://www.zhipin.com/job_detail/aaedd3762cdcabea1nN-2tm5ElVQ.html?lid=4GYxgDQOc1x.search.1&securityId=SdVOfQl3XbUHX-P1vhhD_nZXeMVIQNEF31znM4f_CVVhwBBhMdxBYEt80s9-SJ7el6tfXqgXLHShlt_0uJcjssSs8HZ89mlgIMPr8krIgyIBXj7tEj0u&sessionId=')
# time.sleep(5)
# input("enter:")
# print(driver.page_source)
# driver.close()
