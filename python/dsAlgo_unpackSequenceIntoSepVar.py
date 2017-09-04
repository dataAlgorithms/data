In [1]: p = (4, 5)
In [2]: x, y = p
In [3]: x
Out[3]: 4
In [4]: y
Out[4]: 5
In [12]: data = ['ACME', 50, 91.1, (2012, 12, 21)]

In [13]: data
Out[13]: ['ACME', 50, 91.1, (2012, 12, 21)]
In [14]: name, shares, price, (year, mon, day) = data
In [15]: name
Out[15]: 'ACME'
In [16]: year,
Out[16]: (2012,)
In [17]: mon
Out[17]: 12
In [18]: day
Out[18]: 21

In [21]: s = "hello"
In [22]: a, b, c, d, e = s
In [23]: a
Out[23]: 'h'
In [24]: b
Out[24]: 'e'
In [25]: c
Out[25]: 'l'
In [26]: d
Out[26]: 'l'
In [27]: e
Out[27]: 'o'

In [28]: data = ['ACME', 50, 51.1, (2012, 12, 21)]
In [30]: _, shares, price, _ = data
In [31]: shares
Out[31]: 50
In [32]: price
Out[32]: 51.1
