#coding=utf-8

nobel_winners = [
    {'category': 'Physics',
    'name': 'Albert Einstein',
    'nationality': 'Swiss',
    'sex': 'male',
    'year': 1921},
    {'category': 'Physics',
    'name': 'Paul Dirac',
    'nationality': 'British',
    'sex': 'male',
    'year': 1933},
    {'category': 'Chemistry',
    'name': 'Marie Curie',
    'nationality': 'Polish',
    'sex': 'female',
    'year': 1911}
]

# Write to json file
import json

with open('data/nobel_winners.json', 'w') as f:
    json.dump(nobel_winners, f)

open('data/nobel_winners.json').read()

# Read json file
import json

with open('data/nobel_winners.json') as f:
    nobel_winners = json.load(f)

print(nobel_winners)

# Deal with date and time using json
import datetime
from dateutil import parser
import json

class JSONDateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(self, obj)

def dumps(obj):
    return json.dumps(obj, cls=JSONDateTimeEncoder)

now_str = dumps({'time': datetime.datetime.now()})
print(now_str)

# Turn known format into Python datetime instance
from datetime import datetime
time_str = '2012/01/01 12:32:111'

try:
    dt = datetime.strptime(time_str, '%Y/%m/%d %H:%M:%S')
    print(dt)
except ValueError:
    print('Oops! - invalid date ' + repr(time_str))

'''
C:\Python27\python.exe D:/dataviz/readWriteJsonFile.py
[{u'category': u'Physics', u'nationality': u'Swiss', u'sex': u'male', u'name': u'Albert Einstein', u'year': 1921}, 
{u'category': u'Physics', u'nationality': u'British', u'sex': u'male', u'name': u'Paul Dirac', u'year': 1933}, 
{u'category': u'Chemistry', u'nationality': u'Polish', u'sex': u'female', u'name': u'Marie Curie', u'year': 1911}]

{"time": "2017-10-27T15:19:41.642000"}

Oops! - invalid date '2012/01/01 12:32:111'
'''
