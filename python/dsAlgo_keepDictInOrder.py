from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4


for key in d:
    print(key, d[key])

foo 1
bar 2
spam 3
grok 4

In [20]: import json
In [22]: json.dumps(d)
Out[22]: '{"foo": 1, "bar": 2, "spam": 3, "grok": 4}'
