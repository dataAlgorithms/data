In [20]: a = 4.2

In [21]: b = 2.1

In [22]: a + b
Out[22]: 6.300000000000001

In [23]: (a + b) == 6.3
Out[23]: False

In [24]: from decimal import Decimal

In [25]: a  = Decimal('4.2')

In [26]: b = Decimal('2.1')

In [27]: a + b
Out[27]: Decimal('6.3')

In [28]: print(a + b)
6.3

In [29]: (a + b) == Decimal('6.3')
Out[29]: True

In [30]: from decimal import localcontext

In [31]: a = Decimal('1.3')

In [32]: b = Decimal('1.7')

In [33]: print(a / b)
0.7647058823529411764705882353

In [34]: with localcontext() as ctx:
    ...:     ctx.prec = 3
    ...:     print(a / b)
    ...:
0.765

In [35]: with localcontext() as ctx:
    ...:     ctx.prec = 50
    ...:     print(a / b)
    ...:
0.76470588235294117647058823529411764705882352941176

In [36]: nums = [1.23e+18, 1, -1.23e+18]

In [37]: sum(nums)
Out[37]: 0.0

In [38]: nums = [1.23e+18, 1, 2, -1.23e+18]

In [39]: sum(nums)
Out[39]: 0.0

In [41]: import math

In [42]: math.fsum(nums)
Out[42]: 3.0

In [43]:
