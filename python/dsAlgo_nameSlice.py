In [13]: record = '....................100          .......513.25     ..........'
In [14]: SHARES = slice(20, 32)
In [15]: PRICE = slice(40, 48)
In [16]: cost  = int(record[SHARES]) * float(record[PRICE])
In [17]: print(cost)
51325.0

In [18]: items = [0, 1, 2, 3, 4, 5, 6]
In [19]: a = slice(2, 4)
In [20]: items[a]
Out[20]: [2, 3]
In [21]: items[a] = [10, 11]
In [23]: items
Out[23]: [0, 1, 10, 11, 4, 5, 6]
In [24]: del items[a]
In [25]: items
Out[25]: [0, 1, 4, 5, 6]
In [26]: a = slice(10, 50, 2)
In [27]: a.start
Out[27]: 10
In [28]: a.stop
Out[28]: 50
In [29]: a.step
Out[29]: 2

In [30]: s = 'HelloWorld'
In [31]: a.indices(len(s))
Out[31]: (10, 10, 2)
In [32]: a
Out[32]: slice(10, 50, 2)
In [33]: a.indices(10)
Out[33]: (10, 10, 2)

In [37]: for i in range(*a.indices(len(s))):
    ...:     print(s[i])
    ...:

In [38]: a.indices(len(s))
Out[38]: (10, 10, 2)
