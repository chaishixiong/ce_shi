# -*- coding: utf-8 -*-
import scrapy


class VphSpiderSpider(scrapy.Spider):
    name = 'vph_spider'
    allowed_domains = ['vip.com']
    start_urls = ['http://vip.com/']

    def parse(self, response):
        pass
