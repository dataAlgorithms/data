1. Use item loaders to populate items
import scrapy
from scrapy.loader import ItemLoader

class Product(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)

def parse(self, response):
    l = ItemLoader(item=Product(), response=response)
    l.add_xpath('name', '//div[@class="product_name"]')
    l.add_xpath('name', '//div[@class="product_title"]')
    l.add_xpath('price', '//p[@id="price"]')
    l.add_css('stock', 'p#stock]')
    l.add_value('last_updated', 'today')
    return l.load_item()

2. declare input and output processors
import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags

def filter_price(value):
    if value.isdigit():
        return value

class Product(scrapy.Item):
    name = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )

    price = scrapy.Field(
        input_processor = MapCompose(remove_tags, filter_price),
        output_processor = TakeFirst(),
    )

'''
In [32]: from scrapy.loader import ItemLoader

In [33]: il = ItemLoader(item=Product())

In [34]: il.add_value('name', [u'Welcome to my', u'<strong>website</strong>'])

In [35]: il.add_value('price', [u'&euro;', u'<span>1000</span>'])

In [36]: il.load_item()
Out[36]: {'name': u'Welcome to my website', 'price': u'1000'} 
'''

3. Item loader context
def parse_length(text, loader_context):
    unit = loader_context.get('unit', 'm')
    # ... length parsing code goes here ...
    return parsed_length

4. ItemLoader objects
'''
>>> from scrapy.loader.processors import TakeFirst
>>> loader.get_value(u'name: foo', TakeFirst(), unicode.upper, re='name: (.+)')
'FOO`
'''
loader.add_value('name', u'Color TV')
loader.add_value('colours', [u'white', u'blue'])
loader.add_value('length', u'100')
loader.add_value('name', u'name: foo', TakeFirst(), re='name: (.+)')
loader.add_value(None, {'name': u'foo', 'sex': u'male'})

# HTML snippet: <p class="product-name">Color TV</p>
loader.get_xpath('//p[@class="product-name"]')
# HTML snippet: <p id="price">the price is $1200</p>
loader.get_xpath('//p[@id="price"]', TakeFirst(), re='the price is (.*)')

# HTML snippet: <p class="product-name">Color TV</p>
loader.add_xpath('name', '//p[@class="product-name"]')
# HTML snippet: <p id="price">the price is $1200</p>
loader.add_xpath('price', '//p[@id="price"]', re='the price is (.*)')

# HTML snippet: <p class="product-name">Color TV</p>
loader.get_css('p.product-name')
# HTML snippet: <p id="price">the price is $1200</p>
loader.get_css('p#price', TakeFirst(), re='the price is (.*)')

# HTML snippet: <p class="product-name">Color TV</p>
loader.add_css('name', 'p.product-name')
# HTML snippet: <p id="price">the price is $1200</p>
loader.add_css('price', 'p#price', re='the price is (.*)')

5. nested loader
'''
<footer>
<a class="social" href="http://facebook.com/whatever">Like Us</a>
<a class="social" href="http://twitter.com/whatever">Follow Us</a>
<a class="email" href="mailto:whatever@example.com">Email Us</a>
</footer>
'''

loader = ItemLoader(item=Item())
# load stuff not in the footer
loader.add_xpath('social', '//footer/a[@class = "social"]/@href')
loader.add_xpath('email', '//footer/a[@class = "email"]/@href')
loader.load_item()

loader = ItemLoader(item=Item())
# load stuff not in the footer
footer_loader = loader.nested_xpath('//footer')
footer_loader.add_xpath('social', 'a[@class = "social"]/@href')
footer_loader.add_xpath('email', 'a[@class = "email"]/@href')
# no need to call footer_loader.load_item()
loader.load_item()

6. Reusing and extending item loaders
from scrapy.loader.processors import MapCompose
from myproject.ItemLoaders import ProductLoader
def strip_dashes(x):
    return x.strip('-')

class SiteSpecificLoader(ProductLoader):
    name_in = MapCompose(strip_dashes, ProductLoader.name_in)

from scrapy.loader.processors import MapCompose
from myproject.ItemLoaders import ProductLoader
from myproject.utils.xml import remove_cdata
class XmlProductLoader(ProductLoader):
    name_in = MapCompose(remove_cdata, ProductLoader.name_in)

7. built-processor
'''
# identity
In [37]: from scrapy.loader.processors import Identity

In [38]: proc = Identity()

In [39]: proc(['one', 'two', 'three'])
Out[39]: ['one', 'two', 'three']

# takefirst
In [40]: from scrapy.loader.processors import TakeFirst

In [41]: proc = TakeFirst()

In [42]: proc(['', 'one', 'two', 'three'])
Out[42]: 'one'

# join
In [43]: from scrapy.loader.processors import Join

In [44]: proc = Join()

In [45]: proc(['one', 'two', 'three'])
Out[45]: u'one two three'

In [46]: proc = Join('<br>')

In [47]: proc(['one', 'two', 'three'])
Out[47]: 'one<br>two<br>three'

# compose
In [51]: from scrapy.loader.processors import Compose

In [52]: proc = Compose(lambda v: v[0], str.upper)

In [53]: proc(['hello', 'world'])
Out[53]: 'HELLO'

# mapcompose
In [63]: def filter_world(x):
   ....:     return None if x == 'world' else x
   ....:

In [64]: from scrapy.loader.processors import MapCompose

In [65]: proc = MapCompose(filter_world, unicode.upper)

In [66]: proc([u'hello', u'world', u'this', u'is', u'scrapy'])
Out[66]: [u'HELLO', u'THIS', u'IS', u'SCRAPY']

# selectJmes
>>> from scrapy.loader.processors import SelectJmes, Compose, MapCompose
>>> proc = SelectJmes("foo") #for direct use on lists and dictionaries
>>> proc({'foo': 'bar'})
'bar'
>>> proc({'foo': {'bar': 'baz'}})
{'bar': 'baz'}

>>> import json
>>> proc_single_json_str = Compose(json.loads, SelectJmes("foo"))
>>> proc_single_json_str('{"foo": "bar"}')
u'bar'
>>> proc_json_list = Compose(json.loads, MapCompose(SelectJmes('foo')))
>>> proc_json_list('[{"foo":"bar"}, {"baz":"tar"}]')
[u'bar']
'''
