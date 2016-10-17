#! coding=utf-8 

'''
网页特点:
1. 每个页面上直接有提取的text和author信息,且提取的信息被div[@class="quotes"]包含
2. 下一页的href在class="next"中

网页源码:
    <div class="quote" itemscope itemtype="http://schema.org/CreativeWork">
        <span class="text" itemprop="text">“A woman is like a tea bag; you never know how strong it is until it&#39;s in hot water.”</span>
        <span>by <small class="author" itemprop="author">Eleanor Roosevelt</small>
        <a href="/author/Eleanor-Roosevelt">(about)</a>
        </span>
        <div class="tags">
            Tags:
            <meta class="keywords" itemprop="keywords" content="misattributed-eleanor-roosevelt" /    > 
            
            <a class="tag" href="/tag/misattributed-eleanor-roosevelt/page/1/">misattributed-eleanor-roosevelt</a>
            
        </div>
    </div>

    <div class="quote" itemscope itemtype="http://schema.org/CreativeWork">
        <span class="text" itemprop="text">“A day without sunshine is like, you know, night.”</span>
        <span>by <small class="author" itemprop="author">Steve Martin</small>
        <a href="/author/Steve-Martin">(about)</a>
        </span>
        <div class="tags">
            Tags:
            <meta class="keywords" itemprop="keywords" content="humor,obvious,simile" /    > 
            
            <a class="tag" href="/tag/humor/page/1/">humor</a>
            
            <a class="tag" href="/tag/obvious/page/1/">obvious</a>
            
            <a class="tag" href="/tag/simile/page/1/">simile</a>
            
        </div>
    </div>

    <nav>
        <ul class="pager">
            
            
            <li class="next">
                <a href="/page/2/">Next <span aria-hidden="true">&rarr;</span></a>
            </li>
            
        </ul>
    </nav>
'''
import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotesSpider'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            yield {
                'text': quote.xpath('span[@class="text"]/text()').extract(),
                'author': quote.xpath('span/small[@class="author"]/text()').extract()
            }
            
        next_page = response.xpath('//ul[@class="pager"]/li[@class="next"]/a/@href')
        if next_page:
            next_url = response.urljoin(next_page.extract()[0])
            yield scrapy.Request(next_url, callback=self.parse)