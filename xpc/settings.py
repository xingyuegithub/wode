# -*- coding: utf-8 -*-

# Scrapy settings for xpc project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xpc'

SPIDER_MODULES = ['xpc.spiders']
NEWSPIDER_MODULE = 'xpc.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'xpc (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 2

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True
COOKIES_DEBUG = True
# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False
HTTPPROXY_ENABLED = True
PROXIES = [
    'http://39.106.26.191:1810',
    'http://www.zhouxq.pro:1810',
    'http://47.94.217.179:1810',
    'http://101.201.238.169:1810',
    'http://47.93.186.1:1810',
    'http://47.93.39.4:1810',
    'http://47.93.242.154:1810',
    'http://www.danco.wang:1810',
    'http://39.105.21.19:1810',
    'http://59.110.233.209:1810',
    'http://47.106.153.117:1810',
    'http://47.93.238.37:1810',
    'http://59.110.238.190:1810',
    'http://59.110.174.253:1810',
    'http://www.eastsun.tech:1810',
    'http://47.93.37.63:1810',
    'http://47.106.231.187:1810',
    'http://47.93.39.4:1810',
    'http://47.93.34.43:1810',
    'http://39.106.128.5:1810',
    'http://www.dw4ever.cn:1810',
    'http://47.95.243.220:1810',
    'http://47.93.228.49:1810',
    'http://39.106.131.3:1810',
    'http://www.yins.online:1810',
    'http://47.94.168.29:1810',
    'http://60.205.227.142:1810',
    'http://47.94.254.199:1810',
    'http://47.93.255.212:1810',
    'http://47.93.248.182:1810',
    'http://47.94.93.0:1810',
    'http://114.242.26.51:1810',
    'http://47.94.221.200:1810',
    'http://39.107.121.13:1810',
    'http://140.143.191.23:1810',
]
# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'xpc.middlewares.XpcSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'xpc.middlewares.RandomProxyMiddleware': 749,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'xpc.pipelines.MysqlPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
