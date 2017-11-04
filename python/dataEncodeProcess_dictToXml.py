#codint=utf-8

from xml.etree.ElementTree import Element

# dict of key/value into XML
def dict_to_xml(tag, d):
    '''

    Turn a simple dict of key/value paris into XML
    :param tag:
    :param d:
    :return: xml
    '''

    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)

    return elem

s = {'name':'GOOG', 'shares': 100, 'price':490.1}
e = dict_to_xml('stock', s)
print(e)

# convert Element instance into a byte string
from xml.etree.ElementTree import tostring
print(tostring(e))

# attach attributes to an element
e.set('_id', '1234')
print(tostring(e))

# turn a dict into xml string
def dict_to_xml_str(tag, d):
    parts = ['<{}>'.format(tag)]
    for key, val in d.items():
        parts.append('<{0}>{1}</{0}>'.format(key,val))
    parts.append('</{}>'.format(tag))
    return ''.join(parts)

d = {'name':'<spam>'}
print(dict_to_xml_str('item', d))

# proper xml creation
e = dict_to_xml('item', d)
print(tostring(e))

# manualy escape or unescape special characters
from xml.sax.saxutils import escape, unescape
es = escape('<spam>')
print(es)
print(unescape(es))

'''
D:\Python34\python.exe D:/dataviz/dataEncodeProcess_dictToXml.py
<Element 'stock' at 0x0251D150>
b'<stock><shares>100</shares><price>490.1</price><name>GOOG</name></stock>'
b'<stock _id="1234"><shares>100</shares><price>490.1</price><name>GOOG</name></stock>'
<item><name><spam></name></item>
b'<item><name>&lt;spam&gt;</name></item>'
&lt;spam&gt;
<spam>

Process finished with exit code 0
'''
