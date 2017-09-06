rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

from operator import itemgetter
from itertools import groupby

## -- End pasted text --

In [13]: rows.sort(key=itemgetter('date'))

In [14]: rows
Out[14]:
[{'address': '5412 N CLARK', 'date': '07/01/2012'},
 {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
 {'address': '5800 E 58TH', 'date': '07/02/2012'},
 {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
 {'address': '1060 W ADDISON', 'date': '07/02/2012'},
 {'address': '2122 N CLARK', 'date': '07/03/2012'},
 {'address': '5148 N CLARK', 'date': '07/04/2012'},
 {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}]

In [15]: %paste
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('       ', i)

## -- End pasted text --
07/01/2012
        {'date': '07/01/2012', 'address': '5412 N CLARK'}
        {'date': '07/01/2012', 'address': '4801 N BROADWAY'}
07/02/2012
        {'date': '07/02/2012', 'address': '5800 E 58TH'}
        {'date': '07/02/2012', 'address': '5645 N RAVENSWOOD'}
        {'date': '07/02/2012', 'address': '1060 W ADDISON'}
07/03/2012
        {'date': '07/03/2012', 'address': '2122 N CLARK'}
07/04/2012
        {'date': '07/04/2012', 'address': '5148 N CLARK'}
        {'date': '07/04/2012', 'address': '1039 W GRANVILLE'}

In [16]:
    ...: from collections import defaultdict


In [18]: %paste

rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

## -- End pasted text --

In [19]:
    ...: print(rows_by_date)
defaultdict(<class 'list'>, {'07/02/2012': [{'date': '07/02/2012', 'address': '5
800 E 58TH'}, {'date': '07/02/2012', 'address': '5645 N RAVENSWOOD'}, {'date': '
07/02/2012', 'address': '1060 W ADDISON'}], '07/03/2012': [{'date': '07/03/2012'
, 'address': '2122 N CLARK'}], '07/04/2012': [{'date': '07/04/2012', 'address':
'5148 N CLARK'}, {'date': '07/04/2012', 'address': '1039 W GRANVILLE'}], '07/01/
2012': [{'date': '07/01/2012', 'address': '5412 N CLARK'}, {'date': '07/01/2012'
, 'address': '4801 N BROADWAY'}]})

In [20]: %paste
for r in rows_by_date['07/01/2012']:
    print(r)

## -- End pasted text --
{'date': '07/01/2012', 'address': '5412 N CLARK'}
{'date': '07/01/2012', 'address': '4801 N BROADWAY'}
