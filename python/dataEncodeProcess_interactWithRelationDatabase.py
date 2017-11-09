In [1]: %paste
stocks = [
    ('GOOG', 100, 490.1),
    ('AAPL', 50, 545.75),
    ('FB', 150, 7.45),
    ('HPQ', 75, 33.2),
]

## -- End pasted text --

In [2]: import sqlite3

In [3]: db = sqlite3.connect('database.db')

In [4]: c = db.cursor()

In [5]: c.execute('create table portfolio (symbol text, shares integer, price r
   ...: eal)')
Out[5]: <sqlite3.Cursor at 0x48aea40>

In [6]: db.commit()

In [7]: c.executemany('insert into portfolio values (?,?,?)', stocks)
Out[7]: <sqlite3.Cursor at 0x48aea40>

In [8]: db.commit()

In [9]: for row in db.execute('select * from portfolio'):
   ...:     print(row)
   ...:
('GOOG', 100, 490.1)
('AAPL', 50, 545.75)
('FB', 150, 7.45)
('HPQ', 75, 33.2)

In [10]: min_price = 100

In [11]: for row in db.execute('select * from portfolio where price >= ?', (min
    ...: _price, )):
    ...:     print(row)
    ...:
('GOOG', 100, 490.1)
('AAPL', 50, 545.75)
