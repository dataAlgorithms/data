In [40]: xpts = [1, 5, 4, 2, 10, 7]

In [41]: ypts = [101, 78, 37, 15, 62, 99]

In [42]: for x, y in zip(xpts, ypts):
    ...:     print(x, y)
    ...:
1 101
5 78
4 37
2 15
10 62
7 99

In [43]: a = [1, 2, 3]

In [44]: b = ['w', 'x', 'y', 'z']

In [45]: for i in zip(a, b):
    ...:     print(i)
    ...:
(1, 'w')
(2, 'x')
(3, 'y')

In [46]: from itertools import zip_longest

In [47]: for i  in zip_longest(a, b):
    ...:     print(i)
    ...:
(1, 'w')
(2, 'x')
(3, 'y')
(None, 'z')

In [48]: for i in zip_longest(a, b, fillvalue=0):
    ...:     print(i)
    ...:
(1, 'w')
(2, 'x')
(3, 'y')
(0, 'z')

In [49]: headers = ['name', 'shares', 'price']

In [50]: values = ['ACME', 100, 490.1]

In [51]: s = dict(zip(headers, values))

In [52]: s
Out[52]: {'name': 'ACME', 'price': 490.1, 'shares': 100}

In [54]: for name, val in zip(headers, values):
    ...:     print(name, '=', val)
    ...:
    ...:
name = ACME
shares = 100
price = 490.1

In [55]: a = [1, 2, 3]

In [56]: b = [10, 11, 12]

In [57]: c = ['x', 'y', 'z']

In [58]: for i in zip(a, b, c):
    ...:     print(i)
    ...:
(1, 10, 'x')
(2, 11, 'y')
(3, 12, 'z')

In [59]: zip(a, b)
Out[59]: <zip at 0x4ca09c8>

In [60]: list(zip(a, b))
Out[60]: [(1, 10), (2, 11), (3, 12)]
