In [24]: a = complex(2, 4)

In [25]: b = 3 - 5j

In [26]: a
Out[26]: (2+4j)

In [27]: b
Out[27]: (3-5j)

In [28]: a.real
Out[28]: 2.0

In [29]: a.imag
Out[29]: 4.0

In [30]: a.conjugate()
Out[30]: (2-4j)

In [31]: a + b
Out[31]: (5-1j)

In [32]: a * b
Out[32]: (26+2j)

In [33]: a / b
Out[33]: (-0.4117647058823529+0.6470588235294118j)

In [34]: abs(a)
Out[34]: 4.47213595499958

In [35]: import cmath

In [36]: cmath.sin(a)
Out[36]: (24.83130584894638-11.356612711218174j)

In [37]: cmath.cos(a)
Out[37]: (-11.36423470640106-24.814651485634187j)

In [38]: cmath.exp(a)
Out[38]: (-4.829809383269385-5.5920560936409816j)

In [39]: import numpy as np

In [40]: a = np.array([2+3j, 4+5j, 6-7j, 8+9j])

In [41]: a
Out[41]: array([ 2.+3.j,  4.+5.j,  6.-7.j,  8.+9.j])

In [42]: a + 2
Out[42]: array([  4.+3.j,   6.+5.j,   8.-7.j,  10.+9.j])

In [43]: np.sin(a)
Out[43]:
array([    9.15449915  -4.16890696j,   -56.16227422 -48.50245524j,
        -153.20827755-526.47684926j,  4008.42651446-589.49948373j])

In [44]: import math

In [45]: math.sqrt(-1)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-45-5234f21f3b4d> in <module>()
----> 1 math.sqrt(-1)

ValueError: math domain error

In [46]: import cmath

In [47]: cmath.sqrt(-1)
Out[47]: 1j
