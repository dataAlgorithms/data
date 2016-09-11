#! coding=utf-8 

'''
login done
commnd line argument done
middleware done
chinese
'''

import scrapy
import os
import time
from scrapy.utils.project import get_project_settings
from zhihu.items import ZhihuItem
from scrapy.http import FormRequest
    
settings = get_project_settings() 

class ZhihuSpider(scrapy.Spider):
    name = "zhihu_new"
    start_url = "https://www.zhihu.com"
    login_url = "https://www.zhihu.com/login/email"
    exp_url = "https://www.zhihu.com/explore"
    
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        "Host": "www.zhihu.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36"
    }

    def __init__(self, username=None, password=None):
        '''
        scrapy crawl zhihu -a username="123" -a password="456"
        '''
        if username is None:
            self.username = settings.get('USER_NAME')
        else:
            self.username = username 
            
        if password is None:
            self.password = settings.get('USER_PASSWORD')
        else:
            self.password = password 
            
        self.totalPageCount = 20
        self.currentPage = 0
        self.offset = 10
        self.start = 9
        self._xsrf = None
    def start_requests(self):
        yield scrapy.Request(
            url = self.start_url,
            headers = self.headers,
            meta = {
                'cookiejar':1
            },
            callback = self.request_captcha
        )

    def request_captcha(self, response):
        # get _xsrf
        _xsrf = response.xpath('//input[@name="_xsrf"]/@value').extract()[0]
        self._xsrf = _xsrf
        # the address to get captcha
        captcha_url = 'http://www.zhihu.com/captcha.gif?r=%s&type=login' % str(time.time() * 1000)
        # ready to get captcha
        yield scrapy.Request(
            url = captcha_url,
            headers = self.headers,
            meta = {
                'cookiejar': response.meta['cookiejar'],
                '_xsrf': _xsrf
            },
            callback = self.download_captcha
        )
    
    def download_captcha(self, response):
        # download captcha
        with open('captcha.gif', 'wb') as fp:
            fp.write(response.body)

        os.system('start captcha.gif')
        # Input captcha
        print 'Entry captcha:'
        captcha = raw_input()

        yield scrapy.FormRequest(
            url = self.login_url,
            headers = self.headers,
            formdata = {
                'email': self.username,
                'password': self.password,
                '_xsrf': response.meta['_xsrf'],
                'remember_me': 'true',
                'captcha': captcha
            },
            meta = {
                #'proxy': UsersConfig['proxy'],
                'cookiejar': response.meta['cookiejar']
            },
            callback = self.request_zhihu
        )

    def request_zhihu(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
            
        yield scrapy.Request(
            url = self.exp_url,
            headers = self.headers,
            meta = {
                #'proxy': UsersConfig['proxy'],
                'cookiejar': response.meta['cookiejar'],
                'from': {
                    'sign': 'else',
                    'data': {}
                }
            },
            callback = self.parse_explore,
            dont_filter = True
        )

    def parse_explore(self, response):
        print 'response:', response
        filename = str(self.currentPage) + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
            
        for href in response.xpath('//a[@class="question_link"]/@href'):
            full_url = response.urljoin(href.extract())         
            print 'full_url:', full_url
            yield scrapy.Request(full_url, callback=self.parse_content)
            
            break

        self.currentPage += 1
        yield scrapy.FormRequest(
            url = 'https://www.zhihu.com/node/TopStory2FeedList',
            headers = self.headers,
            formdata = {
                'params': {"offset":'10',"start":'9','_xsrf': self._xsrf},
                #'method': 'next',
            },
            meta = {
                #'proxy': UsersConfig['proxy'],
                'cookiejar': response.meta['cookiejar']
            },
            callback = self.parse_explore
        )
            
    def parse_content(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
            
        item = ZhihuItem()
        item['title'] = response.xpath('//title/text()').extract_first()     
        #item['answer']= response.xpath('//div[@class="zm-editable-content clearfix"]/text()').extract()
        item['link'] = response.url
        
        #print repr(item).decode("unicode-escape") + '\n'
        
        yield item