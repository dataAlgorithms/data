#! coding=utf=8

'''
Important points:

xpath --done
extract/extract_first --done
next_page --done
get text between tag --done
multi process
distribute crawl
pipeline (mysql, mongodb, json)  
crawl spider
'''

import scrapy
import html2text

converter = html2text.HTML2Text()
converter.ignore_links = True

from stackoverflow.items import StackoverflowItem

class StackOverflowSpider(scrapy.Spider):
    name = 'stackoveflow_scrapy'
    start_urls = ['http://stackoverflow.com/questions/tagged/scrapy?sort=votes&pageSize=50']

    def parse(self, response):
        for href in response.xpath('//div[@id="questions"]/div[@class="question-summary"]/div[@class="summary"]/h3/a/@href'):
            full_url = response.urljoin(href.extract())         
            yield scrapy.Request(full_url, callback=self.parse_question)
            
        next_page = response.xpath('//a[@rel="next1"]/@href')
        if next_page:
            next_url = response.urljoin(next_page.extract()[0])
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_question_yield(self, response):
        yield {
            'title': response.xpath('//div[@id="question-header"]/h1/a/text()').extract_first(),     
            'votes': response.xpath('//span[@itemprop="upvoteCount"]/text()').extract_first(),
            'body': converter.handle(response.xpath('//div[@class="post-text"]').extract_first()),
            'tag': response.xpath('//div[@class="post-taglist"]/a/text()').extract(),
            'link': response.url,
        }
        
    def parse_question(self, response):
            item = StackoverflowItem()
            item['title'] = response.xpath('//div[@id="question-header"]/h1/a/text()').extract_first()     
            item['votes']= response.xpath('//span[@itemprop="upvoteCount"]/text()').extract_first()
            item['body'] = converter.handle(response.xpath('//div[@class="post-text"]').extract_first())
            item['tag'] = ','.join(response.xpath('//div[@class="post-taglist"]/a/text()').extract())
            item['link'] = response.url
            yield item