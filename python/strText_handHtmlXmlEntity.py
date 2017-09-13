In [49]: import html

In [50]: print(s)
Elements are written as "<tag>text</tag>".

In [51]: print(html.escape(s))
Elements are written as &quot;&lt;tag&gt;text&lt;/tag&gt;&quot;.

In [52]: print(html.escape(s, quote=False))
Elements are written as "&lt;tag&gt;text&lt;/tag&gt;".

In [53]: s = 'Spicy Jalapeño'

In [55]: s.encode('ascii', errors='xmlcharrefreplace')
Out[55]: b'Spicy Jalape&#241;o'

In [56]: s = 'Spicy &quot;Jalape&#241;o&quot.'

In [57]: from html.parser import HTMLParser

In [58]: p = HTMLParser()

In [59]: p.unescape(s)
d:\Program Files\Anaconda3\Scripts\ipython-script.py:1: DeprecationWarning: The
unescape method is deprecated and will be removed in 3.5, use html.unescape() in
stead.
  if __name__ == '__main__':
Out[59]: 'Spicy "Jalapeño".'

In [62]: from xml.sax.saxutils import unescape

In [63]: unescape(t)
Out[63]: 'The prompt is >>>'
