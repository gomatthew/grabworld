# Scrapy settings for grabworld project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'grabworld'

SPIDER_MODULES = ['grabworld.spiders']
NEWSPIDER_MODULE = 'grabworld.spiders'

HTTPERROR_ALLOW_ALL = True  # http请求异常自己处理

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'grabworld (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 17
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'grabworld.middlewares.GrabworldSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'grabworld.middlewares.GrabworldDownloaderMiddleware': 543,
    'grabworld.middlewares.RandomUserAgentMiddlware': 200,
    'grabworld.middlewares.RandomProxyMiddleware': 300,
}
# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'grabworld.pipelines.GrabworldPipeline': 300,
    # 'grabworld.pipelines.ProxyPipline': 100,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


RANDOM_UA_TYPE = "random"  # ie &google &chrome

# settings for mysql
MYSQL_HOST = "127.0.0.1"
MYSQL_DBNAME = "spider"
MYSQL_USER = "root"
MYSQL_PASSWORD = "makemoney"
MYSQL_PORT = 3306
SQL_ECHO = False

# settings for redis
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
REDIS_DATABASE = 0
REDIS_PASSWORD = ""

# settings for Random proxy
RANDOM_PROXY_FOR_GRAB_PROXY = False
RANDOM_PROXY_FOR_GRAB_BOSS = False
RANDOM_PROXY_FOR_GRAB_TWITTER = False
RANDOM_PROXY_FOR_GRAB_TAOBAO = False
RANDOM_PROXY_FOR_STOCK = True
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'grabworld'))
# sys.path.insert()
if __name__ == '__main__':
    print(BASE_DIR)
# import sys
# import os
# base_dir = os.path.abspath(__file__)
# sys.path.append('/Users/majian/workspace/python/grabworld/utils')
# wget -U 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36' https://tiki.vn/dien-thoai-may-tinh-bang/c1789
