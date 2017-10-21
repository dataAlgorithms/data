//Problem
You want to add or change the Unicode encoding of an already open file without closing
it first.

//Solution
In [20]: import urllib.request

In [21]: import io

In [22]: u = urllib.request.urlopen('http://www.baidu.com')

In [23]: f = io.TextIOWrapper(u, encoding='utf-8')

In [24]: text = f.read()
