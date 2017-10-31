#coding=utf-8

import json

data = {

    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}

# turn python data to json
json_str = json.dumps(data)
print(json_str)

# turn json to python data
data = json.loads(json_str)
print(data)

# write json data
with open('data.json', 'w') as f:
    json.dump(data, f)

# read data back
with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)

# json encoding
d = {'a': True,
     'b': 'Hello',
     'c': None}
print(json.dumps(d))

# keep the order
s = '{"name": "ACME", "shares": 50, "price": 490.1}'
from collections import OrderedDict
data = json.loads(s, object_pairs_hook=OrderedDict)
print(data)

# json dict into python object
class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

data = json.loads(s, object_hook=JSONObject)
print(data.name)
print(data.shares)
print(data.price)

# pretty print
data = json.loads(s, object_pairs_hook=OrderedDict)
print(json.dumps(data))
print(json.dumps(data, indent=4))

# keep key to be sorted
print(json.dumps(data, sort_keys=True))

# serialize instance
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 3)

def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d
classes = {
    'Point': Point
}

def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)
        for key, value in d.items():
            setattr(obj, key, value)
            return obj
    else:
        return d

p = Point(2, 3)
s = json.dumps(p, default=serialize_instance)
print(s)
a = json.loads(s, object_hook=unserialize_object)
print(a)

'''
"D:\Program Files\Anaconda3\python.exe" D:/dataviz/pytest/readWriteJson.py
{"shares": 100, "price": 542.23, "name": "ACME"}
{'shares': 100, 'price': 542.23, 'name': 'ACME'}
{'shares': 100, 'price': 542.23, 'name': 'ACME'}
{"b": "Hello", "c": null, "a": true}
OrderedDict([('name', 'ACME'), ('shares', 50), ('price', 490.1)])
ACME
50
490.1
{"name": "ACME", "shares": 50, "price": 490.1}
{
    "name": "ACME",
    "shares": 50,
    "price": 490.1
}
{"name": "ACME", "price": 490.1, "shares": 50}
{"__classname__": "Point", "y": 3, "x": 2}
<__main__.Point object at 0x0000000000873E48>

Process finished with exit code 0

'''
