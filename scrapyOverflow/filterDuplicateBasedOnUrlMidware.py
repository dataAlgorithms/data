import os

'''
Question:

I am writing a crawler for a website using scrapy with CrawlSpider.

Scrapy provides an in-built duplicate-request filter which filters duplicate requests based on urls. Also, I can filter requests using rules member of CrawlSpider.

What I want to do is to filter requests like:

http:://www.abc.com/p/xyz.html?id=1234&refer=5678
If I have already visited

http:://www.abc.com/p/xyz.html?id=1234&refer=4567
NOTE: refer is a parameter that doesn't affect the response I get, so I don't care if the value of that parameter changes.
Now, if I have a set which accumulates all ids I could ignore it in my callback function parse_item (that's my callback function) to achieve this functionality.

But that would mean I am still at least fetching that page, when I don't need to.

So what is the way in which I can tell scrapy that it shouldn't send a particular request based on the url?

Solution:
add follow filter,

Then you need to set the correct DUPFILTER_CLASS in settings.py

DUPEFILTER_CLASS = 'scraper.duplicate_filter.CustomFilter'

ReferUrl:
http://stackoverflow.com/questions/12553117/how-to-filter-duplicate-requests-based-on-url-in-scrapy
'''

from scrapy.dupefilter import RFPDupeFilter
from scrapy.utils.request import request_fingerprint

class CustomFilter(RFPDupeFilter):
    """A dupe filter that considers specific ids in the url"""

    def __getid(self, url):
        mm = url.split("&refer")[0] #or something like that
        return mm

    def request_seen(self, request):
        fp = self.__getid(request.url)
        if fp in self.fingerprints:
            return True
        self.fingerprints.add(fp)
        if self.file:
            self.file.write(fp + os.linesep)
