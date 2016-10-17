#! coding=utf-8

'''
网页特点:
1. 每页有href,提取的元素需要打开href
2. 有下一页
'''
import scrapy

class AuthorSpider(scrapy.Spider):
    name = 'author'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # follow links to author pages
        #for href in response.css('.author+a::attr(href)').extract():
        for href in response.xpath('//span/small/following-sibling::a[1]/@href').extract():
            yield scrapy.Request(response.urljoin(href),callback=self.parse_author)

        # follow pagination links
        #next_page = response.css('li.next a::attr(href)').extract_first()
        next_page = response.xpath('//ul[@class="pager"]/li[@class="next"]/a/@href').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        def extract_with_xpath(query):
            return response.xpath(query).extract_first().strip()
        
        yield {
            #'name': extract_with_css('h3.author-title::text'),
            #'birthdate': extract_with_css('.author-born-date::text'),
            #'bio': extract_with_css('.author-description::text'),
            'name': extract_with_xpath('//h3[@class="author-title"]/text()'),
            'birthdate': extract_with_xpath('//span[@class="author-born-date"]/text()'),
            'bio': extract_with_xpath('//div[@class="author-description"]/text()'),
        }