# -*- coding: utf-8 -*-
import sys
import os

from scrapy.cmdline import execute

if __name__ == '__main__':

    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    # execute(["scrapy", "crawl", "proxy_bot"])
    execute(["scrapy", "crawl", "tong_hua_shun"])
    # execute(["scrapy", "crawl", "zhihu"])
    # execute(["scrapy", "crawl", "lagou"])

# nohup scrapy runspider ~/workspace/python/grabworld/grabworld/spiders/proxy_spider.py >~/workspace/log/grabworld/proxy.log 2>&1 &