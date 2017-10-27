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

from sqlalchemy import create_engine
engine = create_engine('sqlite:///data/nobel_prize.db', echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

print('\r\n::Define an SQL database table')
from sqlalchemy import Column, Integer, String, Enum

class Winner(Base):
    __tablename__ = 'winners'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    year = Column(Integer)
    nationality = Column(String)
    sex = Column(Enum('male', 'female'))

    def __repr__(self):
        return "<Winner(name='%s', category='%s', year='%s')>"\
         %(self.name, self.category, self.year)

Base.metadata.create_all(engine)

print('\r\n::add instance with a session')
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

albert = Winner(**nobel_winners[0])
session.add(albert)
session.new

winner_rows = [Winner(**w) for w in nobel_winners]
session.add_all(winner_rows)
session.commit()

print('\r\n::query the database')
session.query(Winner).count()

print('\r\n::## query by filter')
result = session.query(Winner).filter_by(nationality='Swiss')
list(result)

print('\r\n::## query by multi filter')
result = session.query(Winner).filter(\
          Winner.category == 'Physics', \
          Winner.nationality != 'Swiss')
list(result)

session.query(Winner).get(3)

print('\r\n::## query by order')
res = session.query(Winner).order_by('year')
list(res)

print('\r\n::## convert instance to a dict')
def inst_to_dict(inst, delete_id=True):
    dat = {}
    for column in inst.__table__.columns:
        dat[column.name] = getattr(inst, column.name)
    if delete_id:
        dat.pop('id')
    return dat

winner_rows = session.query(Winner)
nobel_winners = [inst_to_dict(w) for w in winner_rows]
print(nobel_winners)

print('\r\n::##change object')
marie = session.query(Winner).get(3)
marie.nationality = 'French'
session.dirty
session.commit()
session.dirty

print('\r\n::# delete the result of a query to update database row')
session.query(Winner).filter_by(name='Albert Einstein').delete()
list(session.query(Winner))

# drop the table
# Winner.__table__.drop(engine)

#session.expunge(albert)
#session.new

print("\r\n::use dataset to access mysql")
import dataset

db = dataset.connect('sqlite:///data/nobel_prize.db')

wtable = db['winners']
winners = wtable.find()
winners = list(winners)
print(winners)

'''
winners = db['winners'].find()
dataset.freeze(winners,format='csv', \
         filename='data/nobel_winners_ds.csv')
open('data/nobel_winners_ds.csv').read()

dataset have not method freeze
'''


'''
D:\Anaconda2\python.exe D:/dataviz/readWriteSql.py

::Define an SQL database table
2017-10-27 16:44:37,709 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
2017-10-27 16:44:37,709 INFO sqlalchemy.engine.base.Engine ()
2017-10-27 16:44:37,709 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS VARCHAR(60)) AS anon_1
2017-10-27 16:44:37,709 INFO sqlalchemy.engine.base.Engine ()
2017-10-27 16:44:37,710 INFO sqlalchemy.engine.base.Engine PRAGMA table_info("winners")
2017-10-27 16:44:37,710 INFO sqlalchemy.engine.base.Engine ()

::add instance with a session
2017-10-27 16:44:37,710 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2017-10-27 16:44:37,711 INFO sqlalchemy.engine.base.Engine INSERT INTO winners (name, category, year, nationality, sex) VALUES (?, ?, ?, ?, ?)
2017-10-27 16:44:37,711 INFO sqlalchemy.engine.base.Engine ('Albert Einstein', 'Physics', 1921, 'Swiss', 'male')
2017-10-27 16:44:37,713 INFO sqlalchemy.engine.base.Engine INSERT INTO winners (name, category, year, nationality, sex) VALUES (?, ?, ?, ?, ?)
2017-10-27 16:44:37,713 INFO sqlalchemy.engine.base.Engine ('Albert Einstein', 'Physics', 1921, 'Swiss', 'male')
2017-10-27 16:44:37,713 INFO sqlalchemy.engine.base.Engine INSERT INTO winners (name, category, year, nationality, sex) VALUES (?, ?, ?, ?, ?)
2017-10-27 16:44:37,713 INFO sqlalchemy.engine.base.Engine ('Paul Dirac', 'Physics', 1933, 'British', 'male')
2017-10-27 16:44:37,713 INFO sqlalchemy.engine.base.Engine INSERT INTO winners (name, category, year, nationality, sex) VALUES (?, ?, ?, ?, ?)
2017-10-27 16:44:37,713 INFO sqlalchemy.engine.base.Engine ('Marie Curie', 'Chemistry', 1911, 'Polish', 'female')
2017-10-27 16:44:37,713 INFO sqlalchemy.engine.base.Engine COMMIT

::query the database
2017-10-27 16:44:37,788 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2017-10-27 16:44:37,789 INFO sqlalchemy.engine.base.Engine SELECT count(*) AS count_1 
FROM (SELECT winners.id AS winners_id, winners.name AS winners_name, winners.category AS winners_category, winners.year AS winners_year, winners.nationality AS winners_nationality, winners.sex AS winners_sex 
FROM winners) AS anon_1
2017-10-27 16:44:37,789 INFO sqlalchemy.engine.base.Engine ()

::## query by filter
2017-10-27 16:44:37,792 INFO sqlalchemy.engine.base.Engine SELECT winners.id AS winners_id, winners.name AS winners_name, winners.category AS winners_category, winners.year AS winners_year, winners.nationality AS winners_nationality, winners.sex AS winners_sex 
FROM winners 
WHERE winners.nationality = ?
2017-10-27 16:44:37,793 INFO sqlalchemy.engine.base.Engine ('Swiss',)

::## query by multi filter
2017-10-27 16:44:37,799 INFO sqlalchemy.engine.base.Engine SELECT winners.id AS winners_id, winners.name AS winners_name, winners.category AS winners_category, winners.year AS winners_year, winners.nationality AS winners_nationality, winners.sex AS winners_sex 
FROM winners 
WHERE winners.category = ? AND winners.nationality != ?
2017-10-27 16:44:37,799 INFO sqlalchemy.engine.base.Engine ('Physics', 'Swiss')
2017-10-27 16:44:37,801 INFO sqlalchemy.engine.base.Engine SELECT winners.id AS winners_id, winners.name AS winners_name, winners.category AS winners_category, winners.year AS winners_year, winners.nationality AS winners_nationality, winners.sex AS winners_sex 
FROM winners 
WHERE winners.id = ?
2017-10-27 16:44:37,801 INFO sqlalchemy.engine.base.Engine (3,)

::## query by order
2017-10-27 16:44:37,802 INFO sqlalchemy.engine.base.Engine SELECT winners.id AS winners_id, winners.name AS winners_name, winners.category AS winners_category, winners.year AS winners_year, winners.nationality AS winners_nationality, winners.sex AS winners_sex 
FROM winners ORDER BY winners.year
2017-10-27 16:44:37,802 INFO sqlalchemy.engine.base.Engine ()

::## convert instance to a dict
2017-10-27 16:44:37,803 INFO sqlalchemy.engine.base.Engine SELECT winners.id AS winners_id, winners.name AS winners_name, winners.category AS winners_category, winners.year AS winners_year, winners.nationality AS winners_nationality, winners.sex AS winners_sex 
FROM winners
2017-10-27 16:44:37,803 INFO sqlalchemy.engine.base.Engine ()
[{'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Paul Dirac', 'sex': 'male', 'year': 1933, 'nationality': u'French'}, {'category': u'Chemistry', 'name': u'Marie Curie', 'sex': 'female', 'year': 1911, 'nationality': u'Polish'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Paul Dirac', 'sex': 'male', 'year': 1933, 'nationality': u'British'}, {'category': u'Chemistry', 'name': u'Marie Curie', 'sex': 'female', 'year': 1911, 'nationality': u'Polish'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Paul Dirac', 'sex': 'male', 'year': 1933, 'nationality': u'British'}, {'category': u'Chemistry', 'name': u'Marie Curie', 'sex': 'female', 'year': 1911, 'nationality': u'Polish'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Paul Dirac', 'sex': 'male', 'year': 1933, 'nationality': u'British'}, {'category': u'Chemistry', 'name': u'Marie Curie', 'sex': 'female', 'year': 1911, 'nationality': u'Polish'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Paul Dirac', 'sex': 'male', 'year': 1933, 'nationality': u'British'}, {'category': u'Chemistry', 'name': u'Marie Curie', 'sex': 'female', 'year': 1911, 'nationality': u'Polish'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Paul Dirac', 'sex': 'male', 'year': 1933, 'nationality': u'British'}, {'category': u'Chemistry', 'name': u'Marie Curie', 'sex': 'female', 'year': 1911, 'nationality': u'Polish'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Paul Dirac', 'sex': 'male', 'year': 1933, 'nationality': u'British'}, {'category': u'Chemistry', 'name': u'Marie Curie', 'sex': 'female', 'year': 1911, 'nationality': u'Polish'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Paul Dirac', 'sex': 'male', 'year': 1933, 'nationality': u'British'}, {'category': u'Chemistry', 'name': u'Marie Curie', 'sex': 'female', 'year': 1911, 'nationality': u'Polish'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Paul Dirac', 'sex': 'male', 'year': 1933, 'nationality': u'British'}, {'category': u'Chemistry', 'name': u'Marie Curie', 'sex': 'female', 'year': 1911, 'nationality': u'Polish'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Paul Dirac', 'sex': 'male', 'year': 1933, 'nationality': u'British'}, {'category': u'Chemistry', 'name': u'Marie Curie', 'sex': 'female', 'year': 1911, 'nationality': u'Polish'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Paul Dirac', 'sex': 'male', 'year': 1933, 'nationality': u'British'}, {'category': u'Chemistry', 'name': u'Marie Curie', 'sex': 'female', 'year': 1911, 'nationality': u'Polish'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Paul Dirac', 'sex': 'male', 'year': 1933, 'nationality': u'British'}, {'category': u'Chemistry', 'name': u'Marie Curie', 'sex': 'female', 'year': 1911, 'nationality': u'Polish'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Paul Dirac', 'sex': 'male', 'year': 1933, 'nationality': u'British'}, {'category': u'Chemistry', 'name': u'Marie Curie', 'sex': 'female', 'year': 1911, 'nationality': u'Polish'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Paul Dirac', 'sex': 'male', 'year': 1933, 'nationality': u'British'}, {'category': u'Chemistry', 'name': u'Marie Curie', 'sex': 'female', 'year': 1911, 'nationality': u'Polish'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Paul Dirac', 'sex': 'male', 'year': 1933, 'nationality': u'British'}, {'category': u'Chemistry', 'name': u'Marie Curie', 'sex': 'female', 'year': 1911, 'nationality': u'Polish'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Albert Einstein', 'sex': 'male', 'year': 1921, 'nationality': u'Swiss'}, {'category': u'Physics', 'name': u'Paul Dirac', 'sex': 'male', 'year': 1933, 'nationality': u'British'}, {'category': u'Chemistry', 'name': u'Marie Curie', 'sex': 'female', 'year': 1911, 'nationality': u'Polish'}]

::##change object
2017-10-27 16:44:37,815 INFO sqlalchemy.engine.base.Engine SELECT winners.id AS winners_id, winners.name AS winners_name, winners.category AS winners_category, winners.year AS winners_year, winners.nationality AS winners_nationality, winners.sex AS winners_sex 
FROM winners 
WHERE winners.id = ?
2017-10-27 16:44:37,815 INFO sqlalchemy.engine.base.Engine (3,)
2017-10-27 16:44:37,815 INFO sqlalchemy.engine.base.Engine COMMIT

::# delete the result of a query to update database row
2017-10-27 16:44:37,816 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2017-10-27 16:44:37,818 INFO sqlalchemy.engine.base.Engine SELECT winners.id AS winners_id, winners.name AS winners_name, winners.category AS winners_category, winners.year AS winners_year, winners.nationality AS winners_nationality, winners.sex AS winners_sex 
FROM winners 
WHERE winners.id = ?
2017-10-27 16:44:37,818 INFO sqlalchemy.engine.base.Engine (3,)
2017-10-27 16:44:37,819 INFO sqlalchemy.engine.base.Engine SELECT winners.id AS winners_id, winners.name AS winners_name, winners.category AS winners_category, winners.year AS winners_year, winners.nationality AS winners_nationality, winners.sex AS winners_sex 
FROM winners 
WHERE winners.id = ?
2017-10-27 16:44:37,819 INFO sqlalchemy.engine.base.Engine (61,)
2017-10-27 16:44:37,819 INFO sqlalchemy.engine.base.Engine SELECT winners.id AS winners_id, winners.name AS winners_name, winners.category AS winners_category, winners.year AS winners_year, winners.nationality AS winners_nationality, winners.sex AS winners_sex 
FROM winners 
WHERE winners.id = ?
2017-10-27 16:44:37,819 INFO sqlalchemy.engine.base.Engine (64,)
2017-10-27 16:44:37,819 INFO sqlalchemy.engine.base.Engine DELETE FROM winners WHERE winners.name = ?
2017-10-27 16:44:37,819 INFO sqlalchemy.engine.base.Engine ('Albert Einstein',)
2017-10-27 16:44:37,821 INFO sqlalchemy.engine.base.Engine SELECT winners.id AS winners_id, winners.name AS winners_name, winners.category AS winners_category, winners.year AS winners_year, winners.nationality AS winners_nationality, winners.sex AS winners_sex 
FROM winners
2017-10-27 16:44:37,821 INFO sqlalchemy.engine.base.Engine ()

::use dataset to access mysql
[OrderedDict([('id', 1), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 2), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 3), ('name', u'Paul Dirac'), ('category', u'Physics'), ('year', 1933), ('nationality', u'French'), ('sex', u'male')]), OrderedDict([('id', 4), ('name', u'Marie Curie'), ('category', u'Chemistry'), ('year', 1911), ('nationality', u'Polish'), ('sex', u'female')]), OrderedDict([('id', 5), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 6), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 7), ('name', u'Paul Dirac'), ('category', u'Physics'), ('year', 1933), ('nationality', u'British'), ('sex', u'male')]), OrderedDict([('id', 8), ('name', u'Marie Curie'), ('category', u'Chemistry'), ('year', 1911), ('nationality', u'Polish'), ('sex', u'female')]), OrderedDict([('id', 9), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 10), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 11), ('name', u'Paul Dirac'), ('category', u'Physics'), ('year', 1933), ('nationality', u'British'), ('sex', u'male')]), OrderedDict([('id', 12), ('name', u'Marie Curie'), ('category', u'Chemistry'), ('year', 1911), ('nationality', u'Polish'), ('sex', u'female')]), OrderedDict([('id', 13), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 14), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 15), ('name', u'Paul Dirac'), ('category', u'Physics'), ('year', 1933), ('nationality', u'British'), ('sex', u'male')]), OrderedDict([('id', 16), ('name', u'Marie Curie'), ('category', u'Chemistry'), ('year', 1911), ('nationality', u'Polish'), ('sex', u'female')]), OrderedDict([('id', 17), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 18), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 19), ('name', u'Paul Dirac'), ('category', u'Physics'), ('year', 1933), ('nationality', u'British'), ('sex', u'male')]), OrderedDict([('id', 20), ('name', u'Marie Curie'), ('category', u'Chemistry'), ('year', 1911), ('nationality', u'Polish'), ('sex', u'female')]), OrderedDict([('id', 21), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 22), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 23), ('name', u'Paul Dirac'), ('category', u'Physics'), ('year', 1933), ('nationality', u'British'), ('sex', u'male')]), OrderedDict([('id', 24), ('name', u'Marie Curie'), ('category', u'Chemistry'), ('year', 1911), ('nationality', u'Polish'), ('sex', u'female')]), OrderedDict([('id', 25), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 26), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 27), ('name', u'Paul Dirac'), ('category', u'Physics'), ('year', 1933), ('nationality', u'British'), ('sex', u'male')]), OrderedDict([('id', 28), ('name', u'Marie Curie'), ('category', u'Chemistry'), ('year', 1911), ('nationality', u'Polish'), ('sex', u'female')]), OrderedDict([('id', 29), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 30), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 31), ('name', u'Paul Dirac'), ('category', u'Physics'), ('year', 1933), ('nationality', u'British'), ('sex', u'male')]), OrderedDict([('id', 32), ('name', u'Marie Curie'), ('category', u'Chemistry'), ('year', 1911), ('nationality', u'Polish'), ('sex', u'female')]), OrderedDict([('id', 33), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 34), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 35), ('name', u'Paul Dirac'), ('category', u'Physics'), ('year', 1933), ('nationality', u'British'), ('sex', u'male')]), OrderedDict([('id', 36), ('name', u'Marie Curie'), ('category', u'Chemistry'), ('year', 1911), ('nationality', u'Polish'), ('sex', u'female')]), OrderedDict([('id', 37), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 38), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 39), ('name', u'Paul Dirac'), ('category', u'Physics'), ('year', 1933), ('nationality', u'British'), ('sex', u'male')]), OrderedDict([('id', 40), ('name', u'Marie Curie'), ('category', u'Chemistry'), ('year', 1911), ('nationality', u'Polish'), ('sex', u'female')]), OrderedDict([('id', 41), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 42), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 43), ('name', u'Paul Dirac'), ('category', u'Physics'), ('year', 1933), ('nationality', u'British'), ('sex', u'male')]), OrderedDict([('id', 44), ('name', u'Marie Curie'), ('category', u'Chemistry'), ('year', 1911), ('nationality', u'Polish'), ('sex', u'female')]), OrderedDict([('id', 45), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 46), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 47), ('name', u'Paul Dirac'), ('category', u'Physics'), ('year', 1933), ('nationality', u'British'), ('sex', u'male')]), OrderedDict([('id', 48), ('name', u'Marie Curie'), ('category', u'Chemistry'), ('year', 1911), ('nationality', u'Polish'), ('sex', u'female')]), OrderedDict([('id', 49), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 50), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 51), ('name', u'Paul Dirac'), ('category', u'Physics'), ('year', 1933), ('nationality', u'British'), ('sex', u'male')]), OrderedDict([('id', 52), ('name', u'Marie Curie'), ('category', u'Chemistry'), ('year', 1911), ('nationality', u'Polish'), ('sex', u'female')]), OrderedDict([('id', 53), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 54), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 55), ('name', u'Paul Dirac'), ('category', u'Physics'), ('year', 1933), ('nationality', u'British'), ('sex', u'male')]), OrderedDict([('id', 56), ('name', u'Marie Curie'), ('category', u'Chemistry'), ('year', 1911), ('nationality', u'Polish'), ('sex', u'female')]), OrderedDict([('id', 57), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 58), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 59), ('name', u'Paul Dirac'), ('category', u'Physics'), ('year', 1933), ('nationality', u'British'), ('sex', u'male')]), OrderedDict([('id', 60), ('name', u'Marie Curie'), ('category', u'Chemistry'), ('year', 1911), ('nationality', u'Polish'), ('sex', u'female')]), OrderedDict([('id', 61), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 62), ('name', u'Albert Einstein'), ('category', u'Physics'), ('year', 1921), ('nationality', u'Swiss'), ('sex', u'male')]), OrderedDict([('id', 63), ('name', u'Paul Dirac'), ('category', u'Physics'), ('year', 1933), ('nationality', u'British'), ('sex', u'male')]), OrderedDict([('id', 64), ('name', u'Marie Curie'), ('category', u'Chemistry'), ('year', 1911), ('nationality', u'Polish'), ('sex', u'female')])]

Process finished with exit code 0

'''
