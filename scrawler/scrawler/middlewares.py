# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from collections import defaultdict
import json
import random
from scrawler.settings import IPPOOL

class MyproxiesSpiderMiddleware(object):  
  
      def __init__(self,ip=''):  
          self.ip=ip  
         
      def process_request(self, request, spider):  
          thisip=random.choice(IPPOOL)  
        #   print("this is ip:"+thisip["ipaddr"])  
          request.meta["proxy"]="http://"+thisip["ipaddr"] 

# class RandomHttpProxyMiddleware(HttpProxyMiddleware):


#     def __init__(self, auth_encoding='latin-1', proxy_list_file=None):
#         self.auth_encoding = auth_encoding
#         self.proxies = defaultdict(list)
#         proxy_list_file = "proxy_list.json"
#         print(proxy_list_file)
#         with open(proxy_list_file) as f:
#             proxy_list = json.load(f)
#             for proxy in proxy_list:
#                 scheme = proxy['proxy_scheme']
#                 url = proxy['proxy']
#                 self.proxies['scheme'].append(self._get_proxy(url, scheme))

#         @classmethod
#         def from_crawler(cls, crawler):
#             auth_encoding = crawler.settings.get('HTTPPROXY_AUTH_ENCODING', 'latain-1')
#             proxy_list_file = crawler.settings.get('HTTPPROXY_PROXY_LIST_FILE')
#             return cls(auth_encoding, proxy_list_file)

#         def _set_proxy(self, request, scheme):
#             creds, proxy = random.choice(self.proxies[scheme])
#             request.meta['proxy'] = proxy
#             if creds:
#                 request.headers['Proxy-Authorization'] = b'Basic' + creds


class ScrawlerSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
