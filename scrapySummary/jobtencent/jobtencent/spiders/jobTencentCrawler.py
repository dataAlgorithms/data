# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import Selector
from jobtencent.items import PositionDetailItem
import html2text
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

converter = html2text.HTML2Text()
converter.ignore_links = True

class TencentSpider(CrawlSpider):
    name = "jobTencentCrawler"
    allowed_domains = ["tencent.com"]
    start_urls = [
        "http://hr.tencent.com/position.php"
    ]
    
    rules = [
        Rule(LinkExtractor(allow=("position.php(\?start=[0-9]*)?"), restrict_xpaths=('//a[@id="next"]')), 
                                  callback='parse_start_url', 
                                  follow=True),
    ]
    count = 0
    
    def parse_start_url(self, response):
        #return self.parse(response)
        print '0000000000000'
        print response
        print '0000000000000'
        return self.parse_href(response)
    
    def parse_href(self, response):
        print '111111111111'
        print 'response:', response.url
        print '222222222222'
        for href in response.xpath('//table[@class="tablelist"]/tr[@class="odd" or @class="even"]/td[@class="l square"]/a/@href'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_item)
            
        #next_page = response.xpath('//a[@id="next"]/@href')
        #if next_page:
        #    next_url = response.urljoin(next_page.extract()[0])
        #    yield scrapy.Request(next_url, callback=self.parse)

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