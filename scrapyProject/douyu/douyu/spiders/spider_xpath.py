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


from douyu.items import *
from misc.log import *
from misc.spider import CommonSpider

import pprint
class MyPrettyPrinter(pprint.PrettyPrinter):
    def format(self, object, context, maxlevels, level):
        if isinstance(object, unicode):
            return (object.encode('utf8'), True, False)
        return pprint.PrettyPrinter.format(self, object, context, maxlevels, level)
pp = MyPrettyPrinter()

class douyuSpider(CommonSpider):
    name = "douyu_xpath"
    allowed_domains = ["douyu.com"]
    start_urls = [
        "http://www.douyu.com/directory/all"
    ]
    rules = [
        Rule(sle(allow=("http://www.douyu.com/directory/all")), callback='parse_1', follow=True),
    ]

    list_css_rules = { 
        '#live-list-contentbox li': {
            'url': 'a::attr(href)',
            'room_name': 'a::attr(title)',
            'tag': 'span.tag.ellipsis::text',
            'people_count': '.dy-num.fr::text'
        }
    }

    list_css_rules_for_item = {
        '#live-list-contentbox li': {
            '__use': '1',
            '__list': '1',
            'url': 'a::attr(href)',
            'room_name': 'a::attr(title)',
            'tag': 'span.tag.ellipsis::text',
            'people_count': '.dy-num.fr::text'
        }
    }

    list_xpath_rules_for_item = {
        '//div[@id="live-list-content"]/ul[@id="live-list-contentbox"]/li': {
            'url': './/a/@href',
            'root_name': './/a/@title',
            'tag': './/span[@class="tag ellipsis"]/text()',
            'people_count': './/span[@class="dy-num fr"]/text()'
        }
    }

    def parse_1(self, response):
        info('Parse '+response.url)
        #x = self.parse_with_rules(response, self.list_css_rules, dict)
        x = self.parse_with_rules_xpath(response, self.list_xpath_rules_for_item, dict)
        print 'type(x):', type(x)
        print(len(x))
        # print(json.dumps(x, ensure_ascii=False, indent=2))
        #pp.pprint(x)
        # return self.parse_with_rules(response, self.list_css_rules, douyuItem)
        return x