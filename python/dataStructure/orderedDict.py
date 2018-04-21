In [32]: %paste
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])

## -- End pasted text --
foo 1
bar 2
spam 3
grok 4


说明: 使用OrderedDict会根据放入元素的先后顺序进行排序。所以输出的值是排好序的。
