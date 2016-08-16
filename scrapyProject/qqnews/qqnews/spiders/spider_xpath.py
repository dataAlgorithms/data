# coding=utf-8
import re
import json


from scrapy.selector import Selector
try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle


from qqnews.items import *
from misc.log import *
from misc.spider import CommonSpider


class qqnewsSpider(CommonSpider):
    name = "qqnews_xpath"
    allowed_domains = ["tencent.com", 'qq.com']
    start_urls = [
        'http://news.qq.com/society_index.shtml'
    ]
    rules = [
        Rule(sle(allow=('society_index.shtml')), callback='parse_0', follow=True),
        Rule(sle(allow=(".*[0-9]{8}.*htm$")), callback='parse_1', follow=True),
    ]

    list_xpath_rules = { 
        '//a[@class="linkto"]': {
            'url': '@href',
            'name': 'text()',
        }   
    }
     
    list_css_rules = { 
        '.linkto': {
            'url': 'a::attr(href)',
            'name': 'a::text',
        }   
    }

    list_css_rules_2 = {
        '#listZone .Q-tpWrap': {
            'url': '.linkto::attr(href)',
            'name': '.linkto::text'
        }
    }
    '''
In [36]: print ''.join(response.xpath('//div[@id="Cnt-Main-Article-QQ"]/p/text()
8月11日，家住安徽马鞍山新安花园小区的张女士在自家阳台晒被子时，不慎将丈夫放在其
中的6500元现金抖落，一时间百元大钞“从天而降”，过往路人纷纷捡钱。恰巧，马鞍山雨
山大队执勤交警巡逻至此，现场维持秩序并帮忙找钱，最终和热心人一起找回了5050元。8
月11日8时40分左右，因为天气晴好，家住马鞍山新安花园小区6楼的张女士准备将自家被子
拿出去晒晒，就在她将被子抱到阳台抖开时，裹在里面的6500元现金飘落而下。“丈夫前一
晚放的钱，我自己也不知道。”张女士介绍，晒完被子后，她和往常一样做家务，大概20分
钟后，接到一个邻居打来的电话：“从你家掉出来钱了，怎么回事啊？”随即，张女士从阳
台伸头往下看，当看到地上的钱后，心里顿时慌了。张女士给丈夫打电话，询问被子里放了
多少钱。“里面总共放了6500元现金。”张女士介绍，丈夫平时做点小生意，前一天晚上丈
夫回家后喝了一点酒，因为天气炎热，身上汗多，随手把钱放进了叠好的被子里，第二天早
上还没来得及告诉妻子就出门了。“我当时刚好巡逻经过那里，看到很多人在捡钱。”14日
下午，马鞍山雨山大队交警周晓飞接受记者采访时介绍，当时他沿着雨田路由北向南巡逻。
“你们在干什么，这钱是你们的吗？”周晓飞下车询问，其中一名男子笑了笑，却没有说话
。就在周晓飞询问路人的时候，又有一大片人民币从天上飘下来，有的落到树上，有的落到
院子里，有的落在马路中央。周晓飞得知钱是从楼上掉下来的，赶紧帮忙捡钱，并喊道：“
你们把捡到的钱都交给我，我来交给失主。”周晓飞介绍，当时路面上人越来越多，最多时
有30多人，“如果我不做这件事，就怕过路人捡钱走了。”三五分钟后，总共找回了5050元
现金。
    '''
    content_xpath_rules = {
        'text': '//div[@id="Cnt-Main-Article-QQ"]/p/text()',
        #'images': '#Cnt-Main-Article-QQ img::attr(src)',
        #'images-desc': '#Cnt-Main-Article-QQ div p+ p::text',
    }
    
    content_css_rules = {
        'text': '#Cnt-Main-Article-QQ p *::text',
        #'images': '#Cnt-Main-Article-QQ img::attr(src)',
        #'images-desc': '#Cnt-Main-Article-QQ div p+ p::text',
    }

    def parse_0(self, response):
        info('Parse0 '+response.url)
        x = self.parse_with_rules_xpath(response, self.list_xpath_rules, dict)
        pp.pprint(x)
        #return self.parse_with_rules(response, self.list_css_rules, qqnewsItem)

    def parse_1(self, response):
        info('Parse1 '+response.url)
        x = self.parse_with_rules_xpath(response, self.content_xpath_rules, dict)
        pp.pprint(x)
        return x
        #import pdb; pdb.set_trace()

    def parse_2(self, response):
        info('Parse2 '+response.url)

