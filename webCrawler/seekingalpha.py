#! coding=utf-8 

'''
Page characters:

use ajax to deal with page
page number is increased
   
   http://seekingalpha.com/account/ajax_headlines_content?type=in_focus_articles&page=1&slugs=tsla&is_symbol_page=true
   http://seekingalpha.com/account/ajax_headlines_content?type=in_focus_articles&page=2&slugs=tsla&is_symbol_page=true
   ..

'''

from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.exceptions import CloseSpider
from urlparse import urljoin 
import logging as log 
from scrapy import Selector

import scrapy

class NewsItem(scrapy.Item):
    url = scrapy.Field()
    source = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()

class SeekingAlpha(Spider):
    name = "so"
    download_delay = 0.1

    more_pages = True
    next_page = 1

    start_urls = ['http://seekingalpha.com/account/ajax_headlines_content?type=in_focus_articles&page=0'+
                      '&slugs=tsla&is_symbol_page=true']

    allowed_domains = ['seekingalpha.com']

    def create_ajax_request(self, page_number):
        """
        Helper function to create ajax request for next page.
        """
        ajax_template = 'http://seekingalpha.com/account/ajax_headlines_content?type=in_focus_articles&page={pagenum}&slugs=tsla&is_symbol_page=true'

        url = ajax_template.format(pagenum=page_number)
        return Request(url, callback=self.parse)

    def parse(self, response):
        """
        Parsing of each page.
        """
        if "There are no Focus articles on your stocks." in response.body:
            self.log("About to close spider", log.WARNING)
            raise CloseSpider(reason="no more pages to parse")


        # there is some content extract links to articles
        sel = Selector(response)
        links_xpath = "//div[@class='symbol_article']/a/@href"
        links = sel.xpath(links_xpath).extract()
        for link in links:
            url = urljoin(response.url, link)
            # follow link to article
            # commented out to see how pagination works
            yield Request(url, callback=self.parse_item)

        # generate request for next page
        self.next_page += 1
        yield self.create_ajax_request(self.next_page)

    def parse_item(self, response):
        """
        Parsing of each article page.
        """
        self.log("Scraping: %s" % response.url, level=log.INFO)

        hxs = Selector(response)

        item = NewsItem()

        item['url'] = response.url
        item['source'] = 'seekingalpha'
        item['title'] = hxs.xpath('//title/text()')
        item['date'] = hxs.xpath('//div[@class="article_info_pos"]/span/text()')

        yield item
