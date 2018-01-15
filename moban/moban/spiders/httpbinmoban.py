# -*- coding: utf-8 -*-
import scrapy


class HttpbinmobanSpider(scrapy.Spider):
    name = 'httpbinmoban'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        result=response.body
        print result
