# -*- coding: utf-8 -*-

# Scrapy settings for moban project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'moban'

SPIDER_MODULES = ['moban.spiders']
NEWSPIDER_MODULE = 'moban.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'moban (+http://www.yourdomain.com)'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'itslaw (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept-Encoding':'gzip, deflate, br',
    # 'User-Agent': random_useragent(),
    # 'Referer':'https://www.itslaw.com'
}

# 使用代理
USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 6.1; rv:22.0) Gecko/20130405 Firefox/22.0',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36',
        'Mozilla/5.0 (Windows x86; rv:19.0) Gecko/20100101 Firefox/19.0',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1'
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/5361 (KHTML, like Gecko) Chrome/14.0.860.0 Safari/5361',
        'Mozilla/5.0 (Windows 98; Win 9x 4.90) AppleWebKit/5351 (KHTML, like Gecko) Chrome/15.0.897.0 Safari/5351',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/5330 (KHTML, like Gecko) Chrome/15.0.821.0 Safari/5330',
        'Mozilla/5.0 (Windows; U; Windows NT 5.01) AppleWebKit/533.24.7 (KHTML, like Gecko) Version/4.0.2 Safari/533.24.7'
    ]
HTTPPROXY_ENABLED = True
PROXIES = [
    'http://ms0108:ms0108@182.84.98.201:888',
    'http://ms0108:ms0108@117.41.187.112:888',
    'http://ms0108:ms0108@210.16.189.75:888',
    'http://ms0108:ms0108@1.82.230.108:888',
    'http://ms0108:ms0108@117.41.184.182:888',
    'http://ms0108:ms0108@222.73.48.188:888',
    'http://ms0108:ms0108@103.21.142.201:888',
    ]
# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'itslaw.middlewares.ItslawSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'moban.middlewares.useragent.RandomUserAgentMiddleware':543,
    'moban.middlewares.proxy.RandomProxyMiddleware':749,
   # 'itslaw.middlewares.MyCustomDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
EXTENSIONS = {
   'scrapy.extensions.statsmailer.StatsMailer': 500,
}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'itslaw.pipelines.ItslawPipeline': 300,
# }

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
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

LOG_ENABLED = True
LOG_FILE = BOT_NAME+'.log'
LOG_LEVEL = 'ERROR'
# 发送邮箱信息
MAIL_FROM = 'cyz1071502768@163.com'
MAIL_HOST = 'smtp.163.com'
MAIL_PORT = 25
MAIL_USER = 'cyz1071502768@163.com'
MAIL_PASS = 'zyc123456'
STATSMAILER_RCPTS = '2017283515@qq.com'