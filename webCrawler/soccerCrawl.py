# This spider extracts the info (teams, date-time, score) related to soccer matches from soccerway.com, you can define the cups you want to scrape, the example extracts info related to brazil, but you can add as many tuples you want in the cup list variable, the tuple should have 2 members: the name of the cup and its url in soccerway.com
 
""" soccerway.com spider to scrape soccer matches info """
 
from datetime import datetime
 
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider
from scrapy.item import Item, Field
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import TakeFirst, MapCompose
 
 
class Match(Item):
    """ Item to load with scraped data """
    cup = Field()
    team1 = Field()
    team2 = Field()
    goals1 = Field()
    goals2 = Field()
    date = Field()
    time = Field()
 
 
class MatchLoader(XPathItemLoader):
    """ Loader to make the exctraction easier """
    default_item_class = Match
    default_output_processor = TakeFirst()
    team1_in = MapCompose(lambda x:x.strip())
    team2_in = MapCompose(lambda x:x.strip())
 
 
class SoccerwaySpider(CrawlSpider):
    """ The spider, you can define the cups you want to exctract """
    name = 'soccerway'
    allowed_domains = ['soccerway.com']
    cups = [
        ('brazil-2010',
            'national/brazil/serie-a/2010/regular-season/matches/'),
    ]
 
    def start_requests(self):
        for cup, url in self.cups:
            yield Request('http://www.soccerway.com/%s' % url,
                self.parse_matches, meta={'cup': cup})
 
    def parse_matches(self, response):
        """ Parse the matches in a fixture listing """
        cup = response.request.meta['cup']
 
        xs, dt, dat = HtmlXPathSelector(response), None, None
 
        for tr in xs.select('//table[starts-with(@class,"matches")]'
                '/tbody/tr[not(contains(@class,"aggr"))]'):
            mi = MatchLoader(selector=tr, response=response)
            mi.add_value('cup', cup)
            mi.add_xpath('team1', 'td[3]/a/text()')
            mi.add_xpath('team2', 'td[5]/a/text()')
 
            # Match status info
            sct = [x.strip() for x in tr.select('td[4]//text()').extract() \
                if x.strip()]
            sct = sct[1] if len(sct) > 1 else sct[0]
 
            # Extract timestamp info
            day = tr.select('td[1]/span/text()').extract()
            if day:
                dat = datetime.strptime('%s %s' % (day[0], tr.select(
                    'td[2]/span/text()').extract()[0]), '%a %d/%m/%y')
            if dat:
                mi.add_value('date', dat.strftime('%Y-%m-%d'))
 
            # If not postponed, take the time
            if sct not in ('PSTP', '-'):
                dt = datetime.fromtimestamp(float(
                    tr.select('td[1]/span/@data-value').extract()[0]))
            else:
                dt = None
            if dt:
                mi.replace_value('date', dt.strftime('%Y-%m-%d'))
                mi.add_value('time', dt.strftime('%H:%M'))
 
            # If played, scrape the result
            if '-' in sct:
                goals = [s.strip() for s in sct.split('-')] # 1) strip
                goals = [int(s) for s in goals if s]        # 2) convert to int
                if len(goals) == 2:
                    mi.add_value('goals1', str(goals[0]))
                    mi.add_value('goals2', str(goals[1]))
 
            yield mi.load_item()
 
SPIDER = SoccerwaySpider()
 
# Snippet imported from snippets.scrapy.org (which no longer works)
# author: anibal
# date  : Aug 10, 2010
 
