# -*- coding: utf-8 -*-
import scrapy


class VphSpiderDataSpider(scrapy.Spider):
    name = 'vph_spider_data'
    allowed_domains = ['mapi.vip.com']
    start_urls = ['http://mapi.vip.com/']

    def parse(self, response):
        pass
