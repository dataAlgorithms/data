#-*- coding: utf-8 -*-
'''
gouwu.sogou.com Spider, Created on Dec, 2014
#version: 1.0
#author: chenqx @http://chenqx.github.com
See more: http://doc.scrapy.org/en/latest/index.html
'''
from docutils.utils.math.math2html import URL

'''
from etao.items import EtaoItem

'''

import time
from scrapy.selector import Selector
from scrapy.http import  Request
from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from selenium import webdriver
from scrapy.item import Item, Field

class EtaoItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url   = Field()
    title = Field()
    name = Field()
    price = Field()
    
class etaoSpider(CrawlSpider):
    # name of spiders
    name = 'etaoSpiders'
    allow_domain = ['gouwu.sogou.com']
    start_urls = [ 'http://gouwu.sogou.com/shop?query=' + 'nihao' ]
    link_extractor = {
        'page':  SgmlLinkExtractor(allow = '/detail/\d+\.html.+'),
        'page_down':  SgmlLinkExtractor(allow = '/shop\?query=.+',),#restrict_xpaths = '//a[@class = "pagination-next"]'
    }
    _x_query = {
        'title':   '//p[@class="title"]/a/@title',
        'name':    '//span[@class="floatR hui61 mt1"]/text()',#//li[2]/a/div[@class="ruyitao-market-name ruyitao-market-name-hightlight"]/text()
        'price'    :    '//span[@class="shopprice font17"]/text()', # 'price'    :    '//span[@class = "price"]/text()',
    }
    def __init__(self):
        CrawlSpider.__init__(self)
        # use any browser you wish
        # should download chromedriver.exe into google install directory
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"    
        self.browser = webdriver.Chrome(chromedriver) 
    def __del__(self):
        self.browser.close()
    def parse(self, response):
        #crawl all display page
        for link in self.link_extractor['page_down'].extract_links(response):
            yield Request(url = link.url, callback=self.parse)
        #start browser
        self.browser.get(response.url)
        #loading time interval
        time.sleep(5)
        # get the data and write it to scrapy items
        etaoItem_loader = ItemLoader(item=EtaoItem(), response = response)
        url = str(response.url)
        etaoItem_loader.add_value('url', url)
        etaoItem_loader.add_xpath('title', self._x_query['title'])
        etaoItem_loader.add_xpath('name', self._x_query['name'])
        etaoItem_loader.add_xpath('price', self._x_query['price'])
        yield etaoItem_loader.load_item()
        
'''
Additional URL of selenium with scrapy

http://stackoverflow.com/questions/17975471/selenium-with-scrapy-for-dynamic-page
http://stackoverflow.com/questions/31174330/passing-selenium-response-url-to-scrapy/31186730#31186730
'''
