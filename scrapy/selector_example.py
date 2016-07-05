"""
Selector example
"""

"""
scrapy shell http://doc.scrapy.org/en/latest/_static/selectors-sample1.html


Source code

<html>
 <head>
  <base href='http://example.com/' />
  <title>Example website</title>
 </head>
 <body>
  <div id='images'>
   <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' /></a>
   <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' /></a>
   <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' /></a>
   <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' /></a>
   <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' /></a>
  </div>
 </body>
</html>

"""

'''
# Select the text inside the title tag
response.selector.xpath('//title/text()')
or
response.xpath('//title/text()')
or
response.css('title::text')

# Use css and xpath simultaneously
response.css('img').xpath('@src').extract()
or
resposne.xpath('//img').xpath(@src').extract()
or
response.xpath('//img/@src').extract()

# Extract only first matched element
response.xpath('//div[@id="images"]/a/text()').extract_first()

# Do the check when finding element
response.xpath('//div[@id="not-exists"]/text()').extract_first() is None
response.xpath('//div[@id="not-exists"]/text()').extract_first(default='not-found')

# Get the attribute
response.xpath('//base/@href').extract()
or
response.css('base::attr(href)').extract()

# Contains
response.xpath('//a[contains(@href, "image")]/@href').extract()
or
response.css('a[href*=image]::attr(href)').extract()

response.xpath('//a[contains(@href, "image")]/img/@src').extract()
or
response.css('a[href*=image] img::attr(src)').extract()

//text contains something
//<a href="#">Click here to go to the <strong>Next Page</strong></a>
response.xpath("//a[contains(., 'Next Page')]".extract()

# Nesting selectors
links = response.xpath('//a[contains(@href, "image")]')
links.extract()

for index, link in enumerate(links):
    args = (index,  link.xpath('@href').extract(), link.xpath('img/@src').extract())
    print 'Link number %d points to url %s and image %s' % args

# Selectors with regular expressions
response.xpath('//a[contains(@href, "image")]/text()').re(r'Name:\s*(.*)')
response.xpath('//a[contains(@href, "image")]/text()').re_first(r'Name:\s*(.*)')

response.xpath('//li//@href').extract()
response.xpath('//li[re:test(@class, "item-\d$")]//@href').extract()

# Relative paths
divs = response.xpath('//div')
for img in divs.xpath('.//img'):
    print img.extract()

for a in divs.xpath('a'):
    print a.extract()

# Difference between //node[1] and (//node)[1]
//node[1] selects all the nodes occurring first under their respective parents.
(//node)[1] selects all the nodes in the document, and then gets only the first of them.

In [50]: sel.xpath('//ul/li[1]').extract()
Out[50]: [u'<li>1</li>', u'<li>4</li>']

In [51]: sel.xpath('(//ul/li)[1]').extract()
Out[51]: [u'<li>1</li>']

# Combine css with xpath
In [53]: sel = Selector(text='<div class="hero shout"><time datetime="2014-07-23 19:00">Special date</time>')

In [54]: sel.css('.shout')
Out[54]: [<Selector xpath=u"descendant-or-self::*[@class and contains(concat(' '
, normalize-space(@class), ' '), ' shout ')]" data=u'<div class="hero shout"><ti
me datetime="'>]

In [55]: sel.css('.shout').xpath('./time/@datetime')
Out[55]: [<Selector xpath='./time/@datetime' data=u'2014-07-23 19:00'>]

In [56]: sel.css('.shout').xpath('./time/@datetime').extract()
Out[56]: [u'2014-07-23 19:00']

# remove namespace
scrapy shell https://github.com/blog.atom
In [1]: response.xpath('//link')
Out[1]: []
In [3]: response.selector.remove_namespaces()

In [4]: response.xpath('//link')
Out[4]:
[<Selector xpath='//link' data=u'<link xmlns="http://www.w3.org/2005/Atom'>,
 <Selector xpath='//link' data=u'<link xmlns="http://www.w3.org/2005/Atom'>,
 <Selector xpath='//link' data=u'<link xmlns="http://www.w3.org/2005/Atom'>,
 <Selector xpath='//link' data=u'<link xmlns="http://www.w3.org/2005/Atom'>,
 <Selector xpath='//link' data=u'<link xmlns="http://www.w3.org/2005/Atom'>,
 <Selector xpath='//link' data=u'<link xmlns="http://www.w3.org/2005/Atom'>,
 <Selector xpath='//link' data=u'<link xmlns="http://www.w3.org/2005/Atom'>,
 <Selector xpath='//link' data=u'<link xmlns="http://www.w3.org/2005/Atom'>,
 <Selector xpath='//link' data=u'<link xmlns="http://www.w3.org/2005/Atom'>,
 <Selector xpath='//link' data=u'<link xmlns="http://www.w3.org/2005/Atom'>,
 <Selector xpath='//link' data=u'<link xmlns="http://www.w3.org/2005/Atom'>,
 <Selector xpath='//link' data=u'<link xmlns="http://www.w3.org/2005/Atom'>,
 <Selector xpath='//link' data=u'<link xmlns="http://www.w3.org/2005/Atom'>,
 <Selector xpath='//link' data=u'<link xmlns="http://www.w3.org/2005/Atom'>,
 <Selector xpath='//link' data=u'<link xmlns="http://www.w3.org/2005/Atom'>,
 <Selector xpath='//link' data=u'<link xmlns="http://www.w3.org/2005/Atom'>,
'''