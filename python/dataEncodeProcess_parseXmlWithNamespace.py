'''
cat ns1.xml

<?xml version="1.0" encoding="utf-8"?>
<top>
    <author>David Beazley</author>
    <content>
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <title>Hello World</title>
    </head>
    <body>
    <h1>Hello World!</h1>
    </body>
    </html>
    </content>
</top>
'''

from xml.etree.ElementTree import parse, Element

doc = parse('ns1.xml')

In [4]: print(doc.findtext('author'))
David Beazley

In [5]: print(doc.find('content'))
<Element 'content' at 0x00000000007F39F8>

In [6]: print(doc.find('content/html'))
None

In [7]: print(doc.find('content/{http://www.w3.org/1999/xhtml}html'))
<Element '{http://www.w3.org/1999/xhtml}html' at 0x00000000007F3B38>

In [8]: print(doc.findtext('content/{http://www.w3.org/1999/xhtml}html/head/tit
   ...: le'))
None

In [9]: print( doc.findtext('content/{http://www.w3.org/1999/xhtml}html/{http:/
   ...: /www.w3.org/1999/xhtml}head/{http://www.w3.org/1999/xhtml}title'))
Hello World

class XMLNamespaces:
    def __init__(self, **kwargs):
        self.namespaces = {}
        for name, uri in kwargs.items():
            self.register(name, uri)
    def register(self, name, uri):
        self.namespaces[name] = '{'+uri+'}'
    def __call__(self, path):
        return path.format_map(self.namespaces)

In [11]: ns = XMLNamespaces(html="http://www.w3.org/1999/xhtml")

In [12]: print(doc.find(ns('content/{html}html')))
<Element '{http://www.w3.org/1999/xhtml}html' at 0x00000000007F3B38>

In [13]: print(doc.findtext(ns('content/{html}html/{html}head/{html}title')))
Hello World

'''
>>> from xml.etree.ElementTree import iterparse
>>> for evt, elem in iterparse('ns2.xml', ('end', 'start-ns', 'end-ns')):
...     print(evt, elem)
...
end <Element 'author' at 0x10110de10>
start-ns ('', 'http://www.w3.org/1999/xhtml')
end <Element '{http://www.w3.org/1999/xhtml}title' at 0x1011131b0>
end <Element '{http://www.w3.org/1999/xhtml}head' at 0x1011130a8>
end <Element '{http://www.w3.org/1999/xhtml}h1' at 0x101113310>
end <Element '{http://www.w3.org/1999/xhtml}body' at 0x101113260>
end <Element '{http://www.w3.org/1999/xhtml}html' at 0x10110df70>
end-ns None
end <Element 'content' at 0x10110de68>
end <Element 'top' at 0x10110dd60>
>>> elem # This is the topmost element
<Element 'top' at 0x10110dd60>
>>>
'''
