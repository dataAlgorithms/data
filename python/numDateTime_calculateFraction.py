In [74]: from fractions import Fraction

In [75]: a = Fraction(5, 4)

In [76]: b = Fraction(7, 16)

In [77]: print( a + b )
27/16

In [78]: print( a * b )
35/64

In [79]: c = a *  b

In [80]: c.numerator
Out[80]: 35

In [81]: c.denominator
Out[81]: 64

In [82]: float(c)
Out[82]: 0.546875

In [83]: print(c.limit_denominator(8))
4/7

In [84]: print(c.limit_denominator(5))
1/2

In [85]: x = 3.75

In [86]: y = Fraction(*x.as_integer_ratio())

In [87]: y
Out[87]: Fraction(15, 4)
