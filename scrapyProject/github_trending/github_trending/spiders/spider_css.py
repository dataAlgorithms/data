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

from github_trending.items import *
from misc.log import *
from misc.spider import CommonSpider

import pprint
class MyPrettyPrinter(pprint.PrettyPrinter):
    def format(self, object, context, maxlevels, level):
        if isinstance(object, unicode):
            return (object.encode('utf8'), True, False)
        return pprint.PrettyPrinter.format(self, object, context, maxlevels, level)
pp = MyPrettyPrinter()


class github_trendingSpider(CommonSpider):
    name = "github_trending"
    allowed_domains = ["github.com"]
    start_urls = [
        "http://www.github.com/trending",
    ]
    rules = [
        Rule(sle(allow=("/trending$")), callback='parse_1', follow=True),
    ]

    list_css_rules = { 
        '.repo-list-item': {
            'repo_name': '.repo-list-name a::attr(href)',
            'repo_meta': '.repo-list-meta::text',
        }   
    }   

    content_css_rules = { 
        'text': '#Cnt-Main-Article-QQ p *::text',
        'images': '#Cnt-Main-Article-QQ img::attr(src)',
        'images-desc': '#Cnt-Main-Article-QQ div p+ p::text',
    }

    def parse_1(self, response):
        info('Parse '+response.url)
        x = self.parse_with_rules(response, self.list_css_rules, dict)
        # x = self.parse_with_rules(response, self.content_css_rules, dict)
        #print(json.dumps(x, ensure_ascii=False, indent=2))
        pp.pprint(x)
        # return self.parse_with_rules(response, self.css_rules, github_trendingItem)
        return x