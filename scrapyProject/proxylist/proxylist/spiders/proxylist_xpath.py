# -*- coding: utf-8 -*-
import scrapy

from proxylist.items import *

class ProxylistXpathSpider(scrapy.Spider):
    name = "proxylist_xpath"
    allowed_domains = ["free-proxy-list.net"]
    start_urls = (
        'https://free-proxy-list.net/',
    )

    def parse(self, response):
        items = []

        proxys = response.xpath('//tbody/tr')
        for proxy in proxys:
            item = freeProxyListItem()
            item['ip'] = proxy.xpath('td')[0].xpath('text()').extract()[0]
            item['port'] = proxy.xpath('td')[1].xpath('text()').extract()[0]
            item['code'] = proxy.xpath('td')[2].xpath('text()').extract()[0]
            item['country'] = proxy.xpath('td')[3].xpath('text()').extract()[0]
            item['anonymity'] = proxy.xpath('td')[4].xpath('text()').extract()[0]
            item['google'] = proxy.xpath('td')[5].xpath('text()').extract()[0]
            item['https'] = proxy.xpath('td')[6].xpath('text()').extract()[0]
            item['last_checked'] = proxy.xpath('td')[7].xpath('text()').extract()[0]
            
            items.append(item)
            
        return items