# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['test.com']
    start_urls = ['http://httpbin.org/ip']


    def start_requests(self):  # 控制爬虫发出的第一个请求
        proxy = "http://70E48FDC:BF64B51EEFA7@tunnel5.qg.net:17146"
        meta = {"ownerMemberId": '',
                "productId": '',
                "page": '',
                "proxy": proxy
                }
        yield scrapy.Request(url=self.start_urls[0], meta= meta)

    def parse(self, response):
        print(response.text)
