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


from hrtencent.items import *
from misc.log import *
import html2text

converter = html2text.HTML2Text()
converter.ignore_links = True

class HrtencentSpider(CrawlSpider):
    name = "hrtencent_xpath"
    allowed_domains = ["tencent.com"]
    start_urls = [
        "http://hr.tencent.com/position.php?start=%d" % d for d in range(0, 20, 10)
        #"http://hr.tencent.com/position.php"
    ]
    rules = [
        Rule(sle(allow=("/position_detail.php\?id=\d*.*", )), callback='parse_2'),
        Rule(sle(allow=("/position.php\?&start=\d{,2}#a")), follow=True, callback='parse_1')
    ]

    def start_requests(self):
        requests = list(super(HrtencentSpider, self).start_requests())
        print 'request:',requests 
        return requests

    count = 0
    def parse_2(self, response):
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

    def parse_1(self, response):
        # url cannot encode to Chinese easily.. XXX
        print '11111111111111111111111111111111111111111'
        info('parsed response:' + str(response))

    def _process_request(self, request):
        info('process request:' + str(request))
        return request
