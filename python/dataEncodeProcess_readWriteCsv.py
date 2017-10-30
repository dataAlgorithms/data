######################read operation
'''
stock.csv

Symbol,Price,Date,Time,Change,Volume
"AA",39.48,"6/11/2007","9:36am",-0.18,181800
"AIG",71.38,"6/11/2007","9:36am",-0.15,195500
"AXP",62.58,"6/11/2007","9:36am",-0.46,935000
"BA",98.31,"6/11/2007","9:36am",+0.12,104800
"C",53.08,"6/11/2007","9:36am",-0.25,360900
"CAT",78.29,"6/11/2007","9:36am",-0.23,225400
'''

########### read the data as a sequence of tuple
import csv
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        print(row)

'''
['AA', '39.48', '6/11/2007', '9:36am', '-0.18', '181800']
['AIG', '71.38', '6/11/2007', '9:36am', '-0.15', '195500']
['AXP', '62.58', '6/11/2007', '9:36am', '-0.46', '935000']
['BA', '98.31', '6/11/2007', '9:36am', '+0.12', '104800']
['C', '53.08', '6/11/2007', '9:36am', '-0.25', '360900']
['CAT', '78.29', '6/11/2007', '9:36am', '-0.23', '225400']
'''

########### name the column header
from collections import namedtuple
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r)
        print(row)   # row.Symbol, row.Change to access the elements of each row

'''
Row(Symbol='AA', Price='39.48', Date='6/11/2007', Time='9:36am', Change='-0.18',
 Volume='181800')
Row(Symbol='AIG', Price='71.38', Date='6/11/2007', Time='9:36am', Change='-0.15'
, Volume='195500')
Row(Symbol='AXP', Price='62.58', Date='6/11/2007', Time='9:36am', Change='-0.46'
, Volume='935000')
Row(Symbol='BA', Price='98.31', Date='6/11/2007', Time='9:36am', Change='+0.12',
 Volume='104800')
Row(Symbol='C', Price='53.08', Date='6/11/2007', Time='9:36am', Change='-0.25',
Volume='360900')
Row(Symbol='CAT', Price='78.29', Date='6/11/2007', Time='9:36am', Change='-0.23'
, Volume='225400')
'''

#######name the tuple, and the name may contains whitespace
#######for example: Street Address,Num-Premises,Latitude,Longitude
#######for example: 5412 N CLARK,10,41.980262,-87.66845
import re
with open('stock_re.csv') as f:
    f_csv = csv.reader(f)
    headers = [re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv)]
    Row = namedtuple('Row', headers)
    for r in f_csv:
        row = Row(*r)
        print(row)

########keep the type of data item
col_types = [str, float, str, str, float, int]
with open('stocks_type.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # Apply conversion to the row items
        row = tuple(convert(value) for convert, value in zip(col_types, row))
        print(row)

#######convert selected field of dictionary
field_types = [ ('Price', float),
                ('Change', float),
                ('Volume', int) ]

with open('stocks_dict.csv') as f:
    for row in csv.DictReader(f):
        row.update((key, conversion(row[key]))
                   for key, conversion in field_types)
        print(row)

############# read the data as a sequence of dictionary
import csv
with open('stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row)  # row['Symbol'] row['Change'] to access the elements of each row

'''
{'Price': '39.48', 'Symbol': 'AA', 'Date': '6/11/2007', 'Volume': '181800', 'Tim
e': '9:36am', 'Change': '-0.18'}
{'Price': '71.38', 'Symbol': 'AIG', 'Date': '6/11/2007', 'Volume': '195500', 'Ti
me': '9:36am', 'Change': '-0.15'}
{'Price': '62.58', 'Symbol': 'AXP', 'Date': '6/11/2007', 'Volume': '935000', 'Ti
me': '9:36am', 'Change': '-0.46'}
{'Price': '98.31', 'Symbol': 'BA', 'Date': '6/11/2007', 'Volume': '104800', 'Tim
e': '9:36am', 'Change': '+0.12'}
{'Price': '53.08', 'Symbol': 'C', 'Date': '6/11/2007', 'Volume': '360900', 'Time
': '9:36am', 'Change': '-0.25'}
{'Price': '78.29', 'Symbol': 'CAT', 'Date': '6/11/2007', 'Volume': '225400', 'Ti
me': '9:36am', 'Change': '-0.23'}
'''

###########read tab-separated values csv file
with open('stocks_tab.tsv') as f:
    f_tsv = csv.reader(f, delimiter='\t')
    for row in f_tsv:
        print(row)

#############################write operation
headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
    ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
    ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
]

######### data as a sequence of tuple
with open('stocks_tuple.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)

'''
In [15]: !more stocks_csv.csv
Symbol,Price,Date,Time,Change,Volume
AA,39.48,6/11/2007,9:36am,-0.18,181800
AIG,71.38,6/11/2007,9:36am,-0.15,195500
AXP,62.58,6/11/2007,9:36am,-0.46,935000
'''

############ data as a sequence of dict
headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [{'Symbol':'AA', 'Price':39.48, 'Date':'6/11/2007',
    'Time':'9:36am', 'Change':-0.18, 'Volume':181800},
    {'Symbol':'AIG', 'Price': 71.38, 'Date':'6/11/2007',
    'Time':'9:36am', 'Change':-0.15, 'Volume': 195500},
    {'Symbol':'AXP', 'Price': 62.58, 'Date':'6/11/2007',
    'Time':'9:36am', 'Change':-0.46, 'Volume': 935000},
] 
with open('stocks_dict.csv', 'w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)

'''
In [18]: !more stocks_dict.csv
Symbol,Price,Date,Time,Change,Volume
AA,39.48,6/11/2007,9:36am,-0.18,181800
AIG,71.38,6/11/2007,9:36am,-0.15,195500
AXP,62.58,6/11/2007,9:36am,-0.46,935000
'''
