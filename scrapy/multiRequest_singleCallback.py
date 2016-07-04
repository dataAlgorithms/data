#! *-* coding=utf-8 *-*

import scrapy 

class MySpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['example.com']
    start_urls = [
        'http://www.example.com/1.html',
        'http://www.example.com/2.html',
        'http://www.example.com/3.html',
    ]

    def parse(self, response):
        for h1 in response.xpath('//h1').extract():
            yield {"title": h1}

        for url in response.xpath('//a/@href').extract():
            yield scrapy.Request(url, callback=self.parse)