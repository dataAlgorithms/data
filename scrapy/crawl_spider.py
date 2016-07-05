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
    