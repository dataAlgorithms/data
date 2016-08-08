#!/usr/bin/python 
# -*- coding: utf-8 -*-

import re
import json


from scrapy.selector import Selector
try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle

import scrapy
from hrtencent.items import *
from misc.log import *
import html2text

converter = html2text.HTML2Text()
converter.ignore_links = True

class HrtencentSpider(CrawlSpider):
    name = "hrtencent_own"
    allowed_domains = ["tencent.com"]
    start_urls = [
        "http://hr.tencent.com/position.php"
    ]

    def parse(self, response):
        print '111111111111'
        print 'response:', response
        print '222222222222'
        for href in response.xpath('//table[@class="tablelist"]/tr[@class="odd" or @class="even"]/td[@class="l square"]/a/@href'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_item)
            
        next_page = response.xpath('//a[@id="next"]/@href')
        if next_page:
            next_url = response.urljoin(next_page.extract()[0])
            yield scrapy.Request(next_url, callback=self.parse)
 

    count = 0
    def parse_item(self, response):
        items = []
        sel = Selector(response)
        sites = sel.xpath(u'//table[@class="tablelist textl"]')
        for site in sites:
            item = PositionDetailItem()
            item['sharetitle'] = site.xpath('tr[@class="h"]/td[@id="sharetitle"]/text()').extract() 
            bottom_html = site.xpath('tr[@class="c bottomline"]').extract()[0]
            item['bottomline'] = converter.handle(bottom_html)
            duty_html = site.xpath(u'tr[@class="c"]/td/ul[@class="squareli" and preceding-sibling::div[text()[contains(.,"工作职责")]]]').extract()[0]
            item['duty'] = converter.handle(duty_html)
            requirement_html = site.xpath(u'tr[@class="c"]/td/ul[@class="squareli" and preceding-sibling::div[text()[contains(.,"工作要求")]]]').extract()[0]
            item['requirement'] = converter.handle(requirement_html)
            item['link'] = response.url
            items.append(item)
            
            print repr(item).decode("unicode-escape") + '\n'
        # info('parsed ' + str(response))
        #self.parse_1(response)
        self.count += 1
        print 'count:',self.count
        return items
