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

from pymongo import MongoClient

DB_NOBEL_PRIZE = 'nobel_prize'
COLL_WINNERS = 'winners'

client = MongoClient()
db = client[DB_NOBEL_PRIZE]
coll = db[COLL_WINNERS]

print('\r\n::Accesss a MongoDB database')
from pymongo import MongoClient

def get_mongo_database(db_name, host='localhost',\
              port=27017, username=None, password=None):
    # make mongo connection with/out anthentication
    if username and passowrd:
        mongo_uri = 'mongodb://%s:%s@%s'%\
         (username, password, host, db_name)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)

    return conn[db_name]

db = get_mongo_database(DB_NOBEL_PRIZE)
coll = db[COLL_WINNERS]

print('\r\n::insert record')
coll.insert(nobel_winners)
print(nobel_winners)

print('\r\n::Simple query')
res = coll.find({'category':'Chemistry'})
print(list(res))

print('\r\n::query with compare')
res = coll.find({'year': {'$gt': 1930}})
print(list(res))

print('\r\n::query with mul compare')
res = coll.find({'$or':[{'year': {'$gt': 1930}},\
   {'sex':'female'}]})
print(list(res))

print('\r\n::mongo to dict')
def mongo_coll_to_dicts(dbname='test', collname='test',\
          query={}, del_id=True, **kw):
    db = get_mongo_database(dbname, **kw)
    res = list(db[collname].find(query))

    if del_id:
        for r in res:
            r.pop('_id')

    return res

print(mongo_coll_to_dicts(DB_NOBEL_PRIZE, COLL_WINNERS))

'''
D:\Anaconda2\python.exe D:/dataviz/readWriteMongo.py

::Accesss a MongoDB database

::insert record
[{'category': 'Physics', 'name': 'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': 'Swiss', '_id': ObjectId('59f2f74220d6e24211258f4e')},
{'category': 'Physics', 'name': 'Paul Dirac', 'sex': 'male', 'year': 1933, 'nationality': 'British', '_id': ObjectId('59f2f74220d6e24211258f4f')}, {'category': 'Chemistry', 'name': 'Marie Curie', 'sex': 'female', 'year': 1911, 'nationality': 'Polish', '_id': ObjectId('59f2f74220d6e24211258f50')}]

::Simple query
[{u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish', u'_id': ObjectId('59f2f4bf20d6e232ed1360ea')}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish', u'_id': ObjectId('59f2f4cf20d6e230b157966b')}, 
{u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish', u'_id': ObjectId('59f2f52b20d6e235dd9bcb1a')}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish', u'_id': ObjectId('59f2f53e20d6e23935138c55')},
{u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish', u'_id': ObjectId('59f2f56720d6e23aed77bdcc')}, 
{u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish', u'_id': ObjectId('59f2f5b320d6e238816e0924')}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish', u'_id': ObjectId('59f2f5bf20d6e23d61e97a4f')}, 
{u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish', u'_id': ObjectId('59f2f5cc20d6e23c5160ed02')}, 
{u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish', u'_id': ObjectId('59f2f5dc20d6e229f1c8d2a6')}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish', u'_id': ObjectId('59f2f5e820d6e23e656e09a1')},
{u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish', u'_id': ObjectId('59f2f68220d6e241498ae609')}, 
{u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish', u'_id': ObjectId('59f2f68c20d6e240adc20e5f')}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish', u'_id': ObjectId('59f2f74220d6e24211258f50')}]

::query with compare
[{u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British', u'_id': ObjectId('59f2f4bf20d6e232ed1360e9')}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British', u'_id': ObjectId('59f2f4cf20d6e230b157966a')}, 
{u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British', u'_id': ObjectId('59f2f52b20d6e235dd9bcb19')}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British', u'_id': ObjectId('59f2f53e20d6e23935138c54')}, 
{u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British', u'_id': ObjectId('59f2f56720d6e23aed77bdcb')},
{u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British', u'_id': ObjectId('59f2f5b320d6e238816e0923')}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British', u'_id': ObjectId('59f2f5bf20d6e23d61e97a4e')},
{u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British', u'_id': ObjectId('59f2f5cc20d6e23c5160ed01')},
{u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British', u'_id': ObjectId('59f2f5dc20d6e229f1c8d2a5')}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British', u'_id': ObjectId('59f2f5e820d6e23e656e09a0')}, 
{u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British', u'_id': ObjectId('59f2f68220d6e241498ae608')}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British', u'_id': ObjectId('59f2f68c20d6e240adc20e5e')}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British', u'_id': ObjectId('59f2f74220d6e24211258f4f')}]

::query with mul compare
[{u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British', u'_id': ObjectId('59f2f4bf20d6e232ed1360e9')}, 
{u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish', u'_id': ObjectId('59f2f4bf20d6e232ed1360ea')}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British', u'_id': ObjectId('59f2f4cf20d6e230b157966a')}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish', u'_id': ObjectId('59f2f4cf20d6e230b157966b')}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British', u'_id': ObjectId('59f2f52b20d6e235dd9bcb19')}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish', u'_id': ObjectId('59f2f52b20d6e235dd9bcb1a')}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British', u'_id': ObjectId('59f2f53e20d6e23935138c54')}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish', u'_id': ObjectId('59f2f53e20d6e23935138c55')}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British', u'_id': ObjectId('59f2f56720d6e23aed77bdcb')}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish', u'_id': ObjectId('59f2f56720d6e23aed77bdcc')}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British', u'_id': ObjectId('59f2f5b320d6e238816e0923')}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish', u'_id': ObjectId('59f2f5b320d6e238816e0924')}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British', u'_id': ObjectId('59f2f5bf20d6e23d61e97a4e')}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish', u'_id': ObjectId('59f2f5bf20d6e23d61e97a4f')}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British', u'_id': ObjectId('59f2f5cc20d6e23c5160ed01')}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish', u'_id': ObjectId('59f2f5cc20d6e23c5160ed02')}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British', u'_id': ObjectId('59f2f5dc20d6e229f1c8d2a5')}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish', u'_id': ObjectId('59f2f5dc20d6e229f1c8d2a6')}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British', u'_id': ObjectId('59f2f5e820d6e23e656e09a0')}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish', u'_id': ObjectId('59f2f5e820d6e23e656e09a1')}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British', u'_id': ObjectId('59f2f68220d6e241498ae608')}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish', u'_id': ObjectId('59f2f68220d6e241498ae609')}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British', u'_id': ObjectId('59f2f68c20d6e240adc20e5e')}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish', u'_id': ObjectId('59f2f68c20d6e240adc20e5f')}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British', u'_id': ObjectId('59f2f74220d6e24211258f4f')}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish', u'_id': ObjectId('59f2f74220d6e24211258f50')}]

::mongo to dict
[{u'category': u'Physics', u'name': u'Albert Einstein', u'sex': u'male', u'year': 1921, u'nationality': u'Swiss'}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British'}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish'}, {u'category': u'Physics', u'name': u'Albert Einstein', u'sex': u'male', u'year': 1921, u'nationality': u'Swiss'}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British'}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish'}, {u'category': u'Physics', u'name': u'Albert Einstein', u'sex': u'male', u'year': 1921, u'nationality': u'Swiss'}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British'}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish'}, {u'category': u'Physics', u'name': u'Albert Einstein', u'sex': u'male', u'year': 1921, u'nationality': u'Swiss'}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British'}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish'}, {u'category': u'Physics', u'name': u'Albert Einstein', u'sex': u'male', u'year': 1921, u'nationality': u'Swiss'}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British'}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish'}, {u'category': u'Physics', u'name': u'Albert Einstein', u'sex': u'male', u'year': 1921, u'nationality': u'Swiss'}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British'}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish'}, {u'category': u'Physics', u'name': u'Albert Einstein', u'sex': u'male', u'year': 1921, u'nationality': u'Swiss'}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British'}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish'}, {u'category': u'Physics', u'name': u'Albert Einstein', u'sex': u'male', u'year': 1921, u'nationality': u'Swiss'}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British'}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish'}, {u'category': u'Physics', u'name': u'Albert Einstein', u'sex': u'male', u'year': 1921, u'nationality': u'Swiss'}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British'}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish'}, {u'category': u'Physics', u'name': u'Albert Einstein', u'sex': u'male', u'year': 1921, u'nationality': u'Swiss'}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British'}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish'}, {u'category': u'Physics', u'name': u'Albert Einstein', u'sex': u'male', u'year': 1921, u'nationality': u'Swiss'}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British'}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish'}, {u'category': u'Physics', u'name': u'Albert Einstein', u'sex': u'male', u'year': 1921, u'nationality': u'Swiss'}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British'}, {u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish'}, {u'category': u'Physics', u'name': u'Albert Einstein', u'sex': u'male', u'year': 1921, u'nationality': u'Swiss'}, {u'category': u'Physics', u'name': u'Paul Dirac', u'sex': u'male', u'year': 1933, u'nationality': u'British'}, 
{u'category': u'Chemistry', u'name': u'Marie Curie', u'sex': u'female', u'year': 1911, u'nationality': u'Polish'}]

'''
