In [1]: round(1.23, 1)
Out[1]: 1.2

In [2]: round(1.27, 1)
Out[2]: 1.3

In [3]: round(-1.27, 1)
Out[3]: -1.3

In [4]: round(1.25361, 3)
Out[4]: 1.254

In [5]: a = 1627731

In [6]: round(a, -1)
Out[6]: 1627730

In [7]: round(a, -2)
Out[7]: 1627700

In [8]: round(a, -3)
Out[8]: 1628000

In [9]: x = 1.23456

In [10]: format(x, '0.2f')
Out[10]: '1.23'

In [11]: format(x, '0.3f')
Out[11]: '1.235'

In [12]: 'value is {:0.3f}'.format(x)
Out[12]: 'value is 1.235'

In [13]: a = 2.1

In [14]: b = 4.2

In [15]: c = a + b

In [16]: c
Out[16]: 6.300000000000001

In [17]: c = round(c, 2)

In [18]: c
Out[18]: 6.3

In [19]:
