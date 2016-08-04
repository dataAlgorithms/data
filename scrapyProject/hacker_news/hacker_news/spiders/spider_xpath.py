import re
import json
from urlparse import urlparse
import urllib
import pdb


from scrapy.selector import Selector
try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle


from hacker_news.items import *
from misc.log import *
from misc.spider import CommonSpider

import pprint
class MyPrettyPrinter(pprint.PrettyPrinter):
    def format(self, object, context, maxlevels, level):
        if isinstance(object, unicode):
            return (object.encode('utf8'), True, False)
        return pprint.PrettyPrinter.format(self, object, context, maxlevels, level)
pp = MyPrettyPrinter()

class hacker_newsSpider(CommonSpider):
    count = 0
    name = "hacker_news_xpath"
    allowed_domains = ["news.ycombinator.com"]
    start_urls = [
        "https://news.ycombinator.com",
    ]
    rules = [
        Rule(sle(allow=("/news$")), callback='parse_own', follow=True),
        Rule(sle(allow=("/news\?p=[0-9]*")), callback='parse_own', follow=True),
    ]

    list_xpath_rules = { 
        '//tr[@class="athing"]': {
            'url': './/td[@class="title"]/a[@class="storylink"]/@href',
            'title': './/td[@class="title"]/a/text()',
            #'desc': './/td[@class="subtext"]/span[@class="score"]/text()'
            #'point': '//tr[@class="athing"]/following-sibling::tr[following::tr[@class="spacer"]]/td[@class="subtext"]/span/text()'
        }
    }   

    content_css_rules = { 
        'text': '#Cnt-Main-Article-QQ p *::text',
        'images': '#Cnt-Main-Article-QQ img::attr(src)',
        'images-desc': '#Cnt-Main-Article-QQ div p+ p::text',
    }

    def parse_own(self, response):
        info('parsed ' + str(response))
        items = []
        sel = Selector(response)
        
        '''
        In [28]: response.xpath('//table[@class="itemlist"]/tr[@class="athing"]')[0].xpa
th('following-sibling::tr[following::tr[@class="spacer"]]/td[@class="subtext"]/s
pan[@id="score_12205855"]/text()').extract()

In [20]: response.xpath('//table[@class="itemlist"]/tr[@class="athing"]')[0].xpath('following-sibling::tr[following::tr[@class="spacer"]]/td[@class="subtext"]/a[@class="hnuser" and preceding-sibling::span[@id="score_12211651"]]/text()').ext
Out[20]: [u'OhHeyItsE']

In [25]: response.xpath('//table[@class="itemlist"]/tr[@class="athing"]')[0].xpa
th('following-sibling::tr[following::tr[@class="spacer"]]/td[@class="subtext"]/span/a[contains(@href, "id=12211651")]/text()').extract()
Out[25]: [u'3 hours ago']

In [46]: response.xpath('//table[@class="itemlist"]/tr[@class="athing"]')[0].xpa
th('following-sibling::tr[following::tr[@class="spacer"]]/td[@class="subtext"]/a[re:test(@href, "12211651$")]/text()').extract()
Out[46]: [u'341 comments']
        '''
        sites = sel.xpath('//table[@class="itemlist"]/tr[@class="athing"]')
        print '111111111'
        print 'sites:', sites
        print '222222222'
        for site in sites:
            self.count += 1
            item = hacker_newsItem()
            print 'site:', site
            tid = site.xpath('./@id').extract()[0]
            print 'tid:', tid
            item['res'] = response.url
            item['url'] = site.xpath('./td[@class="title"]/a[@class="storylink"]/@href')[0].extract()
            item['title'] = site.xpath('./td[@class="title"]/a/text()')[0].extract()
            pointsPath = 'following-sibling::tr[following::tr[@class="spacer"]]/td[@class="subtext"]/span[@id="score_%s"]/text()' % str(tid)
            print 'pointsPath:', pointsPath
            item['points'] = site.xpath(pointsPath).extract()
            peoplePath = 'following-sibling::tr[following::tr[@class="spacer"]]/td[@class="subtext"]/a[@class="hnuser" and preceding-sibling::span[@id="score_%s"]]/text()' % str(tid)
            agePath = 'following-sibling::tr[following::tr[@class="spacer"]]/td[@class="subtext"]/span/a[contains(@href, "id=%s")]/text()' % str(tid)
            commentsPath = 'following-sibling::tr[following::tr[@class="spacer"]]/td[@class="subtext"]/a[re:test(@href, "%s$")]/text()' % str(tid)
            item['people'] = site.xpath(peoplePath).extract()
            item['age'] = site.xpath(agePath).extract()
            item['comments'] = site.xpath(commentsPath).extract()
            items.append(item)
        print 'Count:', self.count
        return items
    
    def parse_1(self, response):
        info('Parse '+response.url)
        print 'Count:',self.count
        self.count += 1
        x = self.parse_with_rules_xpath(response, self.list_xpath_rules, dict)
        # x = self.parse_with_rules(response, self.content_css_rules, dict)
        #print(json.dumps(x, ensure_ascii=False, indent=2))
        pp.pprint(x)
            
        return x
        # return self.parse_with_rules(response, self.css_rules, hacker_newsItem)
