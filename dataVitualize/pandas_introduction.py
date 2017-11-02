#!/usr/bin/python

'''
"D:\Program Files\Anaconda3\python.exe" D:/dataviz/pytest/introPandas.py


    category             name nationality     sex  year
0    Physics  Albert Einstein       Swiss    male  1921
1    Physics       Paul Dirac     British    male  1933
2  Chemistry      Marie Curie      Polish  female  1911
Index(['category', 'name', 'nationality', 'sex', 'year'], dtype='object')
RangeIndex(start=0, stop=3, step=1)


category       Physics
nationality      Swiss
sex               male
year              1921
Name: Albert Einstein, dtype: object


category       Chemistry
nationality       Polish
sex               female
year                1911
Name: Marie Curie, dtype: object


category       Chemistry
nationality       Polish
sex               female
year                1911
Name: Marie Curie, dtype: object


category       Physics
nationality      Swiss
sex               male
year              1921
Name: Albert Einstein, dtype: object


<class 'pandas.core.series.Series'>
0      male
1      male
2    female
Name: sex, dtype: object


dict_keys(['Physics', 'Chemistry'])


  category             name nationality   sex  year
0  Physics  Albert Einstein       Swiss  male  1921
1  Physics       Paul Dirac     British  male  1933


0     True
1     True
2    False
Name: category, dtype: bool


  category             name nationality   sex  year
0  Physics  Albert Einstein       Swiss  male  1921
1  Physics       Paul Dirac     British  male  1933

read from multiple item

read from dict


     category              name
0     Physics   Albert Einstein
1   Chemistry       Marie Curie
2  Literature  William Faulkner

write json
None

read json
     category              name
0     Physics   Albert Einstein
1   Chemistry       Marie Curie
2  Literature  William Faulkner

write csv

read csv
   Unnamed: 0    category              name
0           0     Physics   Albert Einstein
1           1   Chemistry       Marie Curie
2           2  Literature  William Faulkner

write dataframes to excel file

write dataframes to shared excel file

read csv into dict

load multiple spreadsheet

return the first datasheet

return a named sheet

all sheet loaded into a name-keyed dictionary

parse up the fifth column

parse the second the fouth columns


0    1
1    2
2    3
3    4
dtype: int64


a    1
b    2
c    3
d    4
dtype: int64


a    1
b    2
c    3
dtype: int64


a    1.0
b    2.0
c    NaN
dtype: float64
****************
a    1
b    2
dtype: int64
****************
a    9
b    9
c    9
dtype: int64
****************
a    1.000000
b    1.414214
c    1.732051
d    2.000000
dtype: float64
b    2
c    3
dtype: int64


0         3
1       5.1
2    foobar
dtype: object


              name   category
0  Albart Einstein    Physics
1      Marie Curie  Chemistry


<class 'pandas.core.panel.Panel'>
Dimensions: 2 (items) x 4 (major_axis) x 4 (minor_axis)
Items axis: item1 to item2
Major_axis axis: 0 to 3
Minor_axis axis: bar to qux
   bar  baz  foo  qux
0    a  NaN    1  NaN
1    b  NaN    2  NaN
2    c  NaN    3  NaN
3  NaN  NaN  NaN  NaN

Process finished with exit code 0

'''

######################################pandas to json
import pandas as pd
import pandas

print("\r\n")
df = pd.read_json('data/nobel_winners.json')
print(df.head())
print(df.columns)
print(df.index)

print("\r\n")
df = df.set_index('name')
print(df.loc['Albert Einstein'])

print("\r\n")
print(df.iloc[2])

print("\r\n")
print(df.ix[2])

print("\r\n")
df = pd.read_json('data/nobel_winners.json')
df = df.set_index('name')
print(df.ix['Albert Einstein'])

print("\r\n")
df = pd.read_json('data/nobel_winners.json')
gender_col = df.sex
print(type(gender_col))
pandas.core.series.Series
print(gender_col.head())

print("\r\n")
df = df.groupby('category')
print(df.groups.keys())

print("\r\n")
phy_group = df.get_group('Physics')
print(phy_group.head())

print("\r\n")
df = pd.read_json('data/nobel_winners.json')
print(df.category == 'Physics')

print("\r\n")
print(df[df.category == 'Physics'])

print("\r\nread from multiple item")
pf = pd.DataFrame({
    'name': ['Albert Einstein', 'Marie Curie','William Faulkner'],
    'category': ['Physics', 'Chemistry', 'Literature']
})

print("\r\nread from dict")
df = pd.DataFrame.from_dict([
    {'name': 'Albert Einstein', 'category':'Physics'},
    {'name': 'Marie Curie', 'category':'Chemistry'},
    {'name': 'William Faulkner', 'category':'Literature'}
])

print("\r\n")
print(df.head())

print("\r\nwrite json")
json = df.to_json('data.json', orient='records')
print(json)

print("\r\nread json")
df = pd.read_json("data.json")
print(df)

######################################pandas to csv
print("\r\nwrite csv")
df = pd.DataFrame.from_dict([
    {'name': 'Albert Einstein', 'category':'Physics'},
    {'name': 'Marie Curie', 'category':'Chemistry'},
    {'name': 'William Faulkner', 'category':'Literature'}
])
df.to_csv('data.csv', encoding='utf-8')

print("\r\nread csv")
df = pd.read_csv('data.csv')
print(df)

'''
from StringIO import StringIO
data = " `Albert Einstein`| Physics \n`Marie Curie`| Chemistry"
df = pd.read_csv(StringIO(data),
sep='|',
names=['name', 'category'],
skipinitialspace=True, quotechar="`")
df
Out:
name category
0 Albert Einstein Physics
1 Marie Curie Chemistry
'''

######################################pandas to excel
print("\r\nwrite dataframes to excel file")
df = pd.DataFrame.from_dict([
    {'name': 'Albert Einstein', 'category':'Physics'},
    {'name': 'Marie Curie', 'category':'Chemistry'},
    {'name': 'William Faulkner', 'category':'Literature'}
])
df.to_excel('nobel_winners.xls', sheet_name='WSheet1')

print("\r\nwrite dataframes to shared excel file")
with pd.ExcelWriter('nobel_winners.xlsx') as writer:
    df.to_excel(writer, sheet_name='WSheet1')
    df.to_excel(writer, sheet_name='WSheet2')
    df.to_excel(writer, sheet_name='WSheet3')

print("\r\nread csv into dict")
dfs = {}
xls = pd.ExcelFile('nobel_winners.xlsx')
dfs['WSheet1'] = xls.parse('WSheet1', na_values=['NA'])
dfs['WSheet2'] = xls.parse('WSheet1', index_col=1,
                                na_values='-',
                                skiprows=3)

print("\r\nload multiple spreadsheet")
data = pd.read_excel('nobel_winners.xlsx', ['WSheet1', 'WSheet2'],
                        index_col=None, na_values=['NA'])

print('\r\nreturn the first datasheet')
df = pd.read_excel('nobel_winners.xlsx')

print("\r\nreturn a named sheet")
df = pd.read_excel('nobel_winners.xlsx', [0, 'WSheet3'])

print("\r\nall sheet loaded into a name-keyed dictionary")
dfs = pd.read_excel('nobel_winners.xlsx', sheetname=None)

print("\r\nparse up the fifth column")
pd.read_excel('nobel_winners.xlsx', 'WSheet1', parse_cols=4)

print("\r\nparse the second the fouth columns")
pd.read_excel("nobel_winners.xlsx", 'WSheet1', parse_cols=[1,3])

'''
######################################pandas to mysql
import sqlalchemy

# create engine to access mysql
engine = sqlalchemy.create_engine(
             'mysql://USER:PASSWORD@localhost/db')

# use pandas to read mysql db
df = pd.read_sql('nobel_winners', engine)

# save DataFrame df to nobel_winners SQL table
df.to_sql('nobel_winners', engine)

# save DataFrame df to nobel_winners SQL table with limitted packet size
df.to_sql('nobel_winners', engine, chunksize=500)  # write 500 rows at a time

# save DataFrame (specity column type)
from sqlalchemy.types import String
df.to_sql('nobel_winners', engine, dtype={'year': String})

'''

######################################pandas to mongodb
import pandas as pd
from pymongo import MongoClient

def get_mongo_database(db_name, host='localhost',\
    port=27017, username=None, password=None):
    """ Get named database from MongoDB with/out authentication """
    # make Mongo connection with/out authentication
    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s/%s'%\
          (username, password, host, db_name)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)
    return conn[db_name]


def mongo_to_dataframe(db_name, collection, query={},\
                     host='localhost', port=27017,\
                     username=None, password=None,\
                     nd_id=True):
    """create a dataframe from mongodb collection"""
    db = get_mongo_database(db_name, host, port, username, password)
    cursor = db[collection].find(query)
    df = pd.DataFrame(list(cursor))

    if no_id:
        del df['_id']

    return df

def dataframe_to_mongo(df, db_name, collection, \
                host='localhost', port=27017,\
                username=None, password=None):
    """save a dataframe to mongodb collection"""
    db = get_mongo_database(db_name, host, port, username, password)
    records = df.to_dict('records')
    db[collection].insert(records)

######################################Series into DataFrames
print("\r\n")
s = pd.Series([1, 2, 3, 4])
print(s)

print("\r\n")
s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s)

print("\r\n")
s = pd.Series({'a':1, 'b':2, 'c':3})
print(s)

print("\r\n")
s = pd.Series({'a':1, 'b':2}, index=['a', 'b', 'c'])
print(s)
print("****************")
s = pd.Series({'a':1, 'b':2, 'c':3}, index=['a', 'b'])
print(s)
print("****************")
s = pd.Series(9, {'a',  'b', 'c'})
print(s)
print("****************")
s = pd.Series([1, 2, 3, 4], ['a', 'b', 'c', 'd'])
import numpy as np
print(np.sqrt(s))

print(s[1:3])

print("\r\n")
s = pd.Series([1, 2.1, 'foo']) + pd.Series([2, 3, 'bar'])
print(s)

print("\r\n")
names = pd.Series(['Albart Einstein', 'Marie Curie'], name='name')
categories = pd.Series(['Physics', 'Chemistry'], name='category')
df = pd.concat([names, categories], axis=1)
print(df.head())

######################################Panel into DataFrames
print("\r\n")
df1 = pd.DataFrame({'foo': [1, 2, 3],
                    'bar': ['a', 'b', 'c']})
df2 = pd.DataFrame({'baz': [7, 8, 9 ,11],
                    'qux': ['p', 'q', 'r', 't']})

pn = pd.Panel({'item1':df1, 'item2':df2})
print(pn)
print(pn['item1'])
