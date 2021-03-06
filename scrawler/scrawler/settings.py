# -*- coding: utf-8 -*-

# Scrapy settings for scrawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import os

BOT_NAME = 'scrawler'

SPIDER_MODULES = ['scrawler.spiders']
NEWSPIDER_MODULE = 'scrawler.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# 第二个数字代表优先级(1-1000)，数字越低，优先级越高
ITEM_PIPELINES = {
	'scrawler.pipelines.ScrawlerPipeline': 1,
	'scrawler.pipelines.MyImagePipeline': 1
}

# 下载器中间件
# DOWNLOADER_MIDDLEWARES = {
# 	# 置于HttpProxyMiddleware(750)之前
# 	'scrawler.middlewares.RandomHttpProxyMiddleware':745
# }
# DOWNLOADER_MIDDLEWARES = {
#      'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware':543,
#      'scrawler.middlewares.MyproxiesSpiderMiddleware':125
# }

# 配置代理文件
HTTPPROXY_PROXY_LIST_FILE='proxy_list.json'

IMAGES_STORE = "/home/qh/git/comic_crawler/scrawler/scrawler/images/"
# request并发数
CONCURRENT_REQUESTS = 100

# 日志级别
# LOG_LEVEL = 'INFO'
# LOG_LEVEL = 'DEBUG'
LOG_LEVEL = 'INFO'

# 关闭cookie，提高性能
COOKIES_ENABLED = False

# 禁止重试
RETRY_ENABLED = False

# 减少下载超时
DOWNLOAD_TIMEOUT = 500

# 禁止重定向
REDIRECT_ENABLED = False

# 图片存储地址
IMAGES_DIR = os.getcwd()


# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scrawler.middlewares.ScrawlerSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'scrawler.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'scrawler.pipelines.ScrawlerPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings

HTTPCACHE_ENABLED = False
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'

# vultr
# 45.77.126.21  22 Los Angeles
# 207.246.122.70 22 New Jersey

# linode
# 45.33.37.117 28999 Fremont, CA, USA
# 139.162.113.67 japan

# banwagong
# 67.218.159.92 28908 Los Angeles


## 代理服务器配置
# 主服务器
# 67.218.159.92
# 代理
# 45.77.126.21:9888
# 207.246.122.70:9888
# 45.33.37.117:9888
# 139.162.113.67:9888

IPPOOL=[
	{"ipaddr":"45.77.126.21:9888"},
	{"ipaddr":"207.246.122.70:9888"},
	{"ipaddr":"45.33.37.117:9888"},
	{"ipaddr":"139.162.113.67:9888"}
]