from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)

//output
Subscriber(addr='jonesy@example.com', joined='2012-10-19')
jonesy@example.com
2012-10-19

addr, joined = sub
print(addr)
print(joined)

//output
jonesy@example.com
2012-10-19

Stock = namedtuple('Stock', ['name', 'shares', 'price'])

def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

s = Stock('ACME', 100, 123.45)
print(s)

//output
Stock(name='ACME', shares=100, price=123.45)

s.shares = 75

//output
AttributeError: can't set attribute

s = s._replace(shares=75)
print(s)

//output
Stock(name='ACME', shares=75, price=123.45)

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0.0, None, None)

def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))

//output
Stock(name='ACME', shares=100, price=123.45, date=None, time=None)

b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))

//output
Stock(name='ACME', shares=100, price=123.45, date='12/17/2012', time=None)
