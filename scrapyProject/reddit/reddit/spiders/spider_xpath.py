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


from reddit.items import *
from misc.log import *
from misc.spider import CommonSpider


class redditSpider(CommonSpider):
    name = "reddit_xpath"
    allowed_domains = ["reddit.com"]
    start_urls = [
        "https://www.reddit.com/",
    ]
    rules = [
        Rule(sle(allow=("https://www.reddit.com/")), callback='parse_1', follow=True),
    ]

    list_css_rules = { 
        '.link': {
            'title': '.title a::text',
            'domain': '.domain a::text',
            'author': '.author::text',
            'comment_count': '.comments::text',
            'score': '.score::text',
        }   
    }   

    content_css_rules = { 
        'text': '#Cnt-Main-Article-QQ p *::text',
        'images': '#Cnt-Main-Article-QQ img::attr(src)',
        'images-desc': '#Cnt-Main-Article-QQ div p+ p::text',
    }

    list_xpath_rules = { 
        '//div[@class="entry unvoted"]': {
            'title': 'p[@class="title"]/a/text()',
            'domain': 'p[@class="title"]/span[@class="domain"]/a/text()',
            'author': 'p[@class="tagline"]/a[contains(@class, "author")]/text()',
            'comment_count': 'ul[@class="flat-list buttons"]/li[@class="first"]/a/text()',
        }   
    }  
    
    def parse_1(self, response):
        info('Parse '+response.url)
        x = self.parse_with_rules_xpath(response, self.list_xpath_rules, dict)
        # x = self.parse_with_rules(response, self.content_css_rules, dict)
        print(json.dumps(x, ensure_ascii=False, indent=2))
        # pp.pprint(x)
        # return self.parse_with_rules(response, self.css_rules, redditItem)
        return x