# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from hackernews.items import HackernewsItem
from scrapy.selector import Selector
import logging

class HackernewsspiderSpider(CrawlSpider):
    name = 'hackerNewsSpider'
    allowed_domains = ['news.ycombinator.com']
    start_urls = ['https://news.ycombinator.com/']

    rules = [
        Rule(LinkExtractor(allow=("/news$")), callback='parse_own', follow=True),
        Rule(LinkExtractor(allow=("/news\?p=[0-9]*")), callback='parse_own', follow=True),
    ]
    
    count = 0
    
    def parse_own(self, response):
        logging.info('parsed ' + str(response))
        items = []
        sel = Selector(response)
        
        '''
        <tr class='athing' id='12481700'>
    <td align="right" valign="top" class="title">
        <span class="rank">1.</span></td>
    <td valign="top" class="votelinks">
        <center>
            <a id='up_12481700' href='vote?id=12481700&amp;how=up&amp;goto=news'>
                <div class='votearrow' title='upvote'></div>
            </a>
        </center>
    </td>
    <td class="title">
        <a href="http://www.mono-project.com/news/2016/09/12/arm64-icache/" class="storylink">A tale of an impossible bug: big.LITTLE and caching</a>
        <span class="sitebit comhead">(
            <a href="from?site=mono-project.com">
                <span class="sitestr">mono-project.com</span></a>)</span>
    </td>
</tr>
<tr>
    <td colspan="2"></td>
    <td class="subtext">
        <span class="score" id="score_12481700">283 points</span>by
        <a href="user?id=rodrigokumpera" class="hnuser">rodrigokumpera</a>
        <span class="age">
            <a href="item?id=12481700">4 hours ago</a></span>
        <span id="unv_12481700"></span>|
        <a href="hide?id=12481700&amp;goto=news">hide</a>|
        <a href="item?id=12481700">58&nbsp;comments</a></td>
</tr>
<tr class="spacer" style="height:5px"></tr>
<tr class='athing' id='12482209'>
    <td align="right" valign="top" class="title">
        <span class="rank">2.</span></td>
    <td valign="top" class="votelinks">
        <center>
            <a id='up_12482209' href='vote?id=12482209&amp;how=up&amp;goto=news'>
                <div class='votearrow' title='upvote'></div>
            </a>
        </center>
    </td>
    <td class="title">
        <a href="http://www.righto.com/2016/09/restoring-ycombinators-xerox-alto-day-6.html" class="storylink">Restoring YC's Xerox Alto, Day 6: Fixed a chip, data read from disk</a>
        <span class="sitebit comhead">(
            <a href="from?site=righto.com">
                <span class="sitestr">righto.com</span></a>)</span>
    </td>
</tr>
<tr>
    <td colspan="2"></td>
    <td class="subtext">
        <span class="score" id="score_12482209">92 points</span>by
        <a href="user?id=mr_golyadkin" class="hnuser">mr_golyadkin</a>
        <span class="age">
            <a href="item?id=12482209">3 hours ago</a></span>
        <span id="unv_12482209"></span>|
        <a href="hide?id=12482209&amp;goto=news">hide</a>|
        <a href="item?id=12482209">11&nbsp;comments</a></td>
</tr>
<tr class="spacer" style="height:5px"></tr>

        In [28]: response.xpath('//table[@class="itemlist"]/tr[@class="athing"]')[0].xpa
th('following-sibling::tr[following::tr[@class="spacer"]]/td[@class="subtext"]/s
pan[@id="score_12205855"]/text()').extract()

In [20]: response.xpath('//table[@class="itemlist"]/tr[@class="athing"]')[0].xpath('following-sibling::tr[following::tr[@class="spacer"]]/td[@class="subtext"]/a[@class="hnuser" and preceding-sibling::span[@id="score_12211651"]]/text()').ext
Out[20]: [u'OhHeyItsE']

In [25]: response.xpath('//table[@class="itemlist"]/tr[@class="athing"]')[0].xpa
th('following-sibling::tr[following::tr[@class="spacer"]]/td[@class="subtext"]/span/a[contains(@href, "id=12211651")]/text()').extract()
Out[25]: [u'3 hours ago']

In [46]: response.xpath('//table[@class="itemlist"]/tr[@class="athing"]')[0].xpa
th('following-sibling::tr[following::tr[@class="spacer"]]/td[@class="subtext"]/a[re:test(@href, "12211651$")]/text()').extract()
Out[46]: [u'341 comments']
        '''
        sites = sel.xpath('//table[@class="itemlist"]/tr[@class="athing"]')
        for site in sites:
            self.count += 1
            item = HackernewsItem()
            tid = site.xpath('./@id').extract()[0]
            item['res'] = response.url
            item['url'] = site.xpath('./td[@class="title"]/a[@class="storylink"]/@href')[0].extract()
            item['title'] = site.xpath('./td[@class="title"]/a/text()')[0].extract()
            pointsPath = 'following-sibling::tr[following::tr[@class="spacer"]]/td[@class="subtext"]/span[@id="score_%s"]/text()' % str(tid)
            item['points'] = site.xpath(pointsPath).extract()
            peoplePath = 'following-sibling::tr[following::tr[@class="spacer"]]/td[@class="subtext"]/a[@class="hnuser" and preceding-sibling::span[@id="score_%s"]]/text()' % str(tid)
            agePath = 'following-sibling::tr[following::tr[@class="spacer"]]/td[@class="subtext"]/span/a[contains(@href, "id=%s")]/text()' % str(tid)
            commentsPath = 'following-sibling::tr[following::tr[@class="spacer"]]/td[@class="subtext"]/a[re:test(@href, "%s$")]/text()' % str(tid)
            item['people'] = site.xpath(peoplePath).extract()
            item['age'] = site.xpath(agePath).extract()
            item['comments'] = site.xpath(commentsPath).extract()
            items.append(item)
        print 'Count:', self.count
        return items