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


from alexa_topsites.items import *
from misc.log import *
from misc.spider import CommonSpider


class alexa_topsitesSpider(CommonSpider):
    name = "alexa_topsites_xpath"
    allowed_domains = ["alexa.com"]
    start_urls = [
        "http://www.alexa.com/topsites",
    ]
    rules = [
        Rule(sle(allow=("http://www.alexa.com/topsites")), callback='parse_1', follow=True),
    ]

    list_xpath_rules = { 
        '//li[@class="site-listing"]': {
            'rank': './/div[@class="count"]/text()',
            'name': './/div[@class="desc-container"]/p[@class="desc-paragraph"]/a/text()',
            'desc': './/div[@class="desc-container"]/div[@class="description"]/text()'
        }   
    }   

    content_css_rules = { 
        'text': '#Cnt-Main-Article-QQ p *::text',
        'images': '#Cnt-Main-Article-QQ img::attr(src)',
        'images-desc': '#Cnt-Main-Article-QQ div p+ p::text',
    }

    def parse_1(self, response):
        info('Parse '+response.url)
        x = self.parse_with_rules_xpath(response, self.list_xpath_rules, dict)
        # x = self.parse_with_rules(response, self.content_css_rules, dict)
        print(json.dumps(x, ensure_ascii=False, indent=2))
        # pp.pprint(x)
        # return self.parse_with_rules(response, self.css_rules, alexa_topsitesItem)
