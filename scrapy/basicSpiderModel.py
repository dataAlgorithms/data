1. crawl spider model
#! *-* coding=utf-8 *-*

"""
This spider would start crawling example.com’s home page, collecting category links, and item links, parsing the latter
with the parse_item method. For each item response, some data will be extracted from the HTML using XPath,
and an Item will be filled with it.
"""

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com']

    rules = (
        # Extract links matching category.php (but not matching subsection.php)
        # and follow links from them (since no callback means follow=True by default)
        Rule(LinkExtractor(allow=('category\.php',), deny=('subsection\.php', ))),

        # Extract links matching item.php and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=('item\.php',)), callback='parse_item'),
    )

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        item = scrapy.Item()
        item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        item['name'] = response.xpath('//td[@id="item_name"]/text()').extract()
        item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
        return item
        
2. csv spider model
from scrapy.spiders import CSVFeedSpider
import scrapy 

class MySpider(CSVFeedSpider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com/feed.csv']
    delimiter = ';'
    quotechar = "'"
    headers = ['id', 'name', 'description']

    def parse_row(self, response, row):
        self.logger.info('Hi, this is a row %r', row)

        item = scrapy.Item()
        item['id'] = row['id']
        item['name'] = row['name']
        item['description'] = row['description']
        return item
        
3. sitemap spider model
# different callback
from scrapy.spiders import SitemapSpider

class MySpider(SitemapSpider):
    sitemap_urls = ['http://www.example.com/sitemap.xml']
    sitemap_rules = [
        ('/product/', 'parse_product'),
        ('/category/', 'parse_category'),
    ]

    def parse_product(self, response):
        pass

    def parse_category(self, response):
        pass
        
# parse callback
from scrapy.spiders import SitemapSpider

class MySpider(SitemapSpider):
    sitemap_urls = ['http://www.example.com/sitemap.xml']

    def parse(self, response):
        pass
        
# robots
from scrapy.spiders import SitemapSpider

class MySpider(SitemapSpider):
    sitemap_urls = ['http://www.example.com/robots.txt']
    sitemap_rules = [
        ('/shop/', 'parse_shop'),
    ]
    sitemap_follow = ['/sitemap_shops']
    def parse_shop(self, response):
        pass
        
# with other url
from scrapy.spiders import SitemapSpider
import scrapy 

class MySpider(SitemapSpider):
    sitemap_urls = ['http://www.example.com/robots.txt']
    sitemap_rules = [
        ('/shop/', 'parse_shop'),
    ]
    
    other_ursl = ['http://www.example.com/about']

    def start_requests(self):
        requests = list(super(MySpider, self).start_requests())
        requests += [scrapy.Request(x, self.parse_other) for x in self.other_urls]
        return requests

    def parse_shop(self, response):
        pass

    def parse_other(self, response):
        pass

4. xml spider
#! *-* coding=utf-8 *-*

from scrapy.spiders import XMLFeedSpider
import scrapy 

class MySpider(XMLFeedSpider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_ursl = ['http://www.example.com/feed.xml']
    iterator = 'iternodes'
    itertag = 'item'

    def parse_node(self, response, node):
        self.logger.info('Hi, this is a <%s> node! %s', self.itertag, ''.join(node.extract()))

        item = scrapy.Item()
        item['id'] = node.xpath('@id').extract()
        item['name'] = node.xpath('name').extract()
        item['description'] = node.xpath('description').extract()
        return item
