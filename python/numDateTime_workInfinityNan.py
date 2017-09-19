In [48]: a = float('inf')

In [49]: b = float('-inf')

In [50]: c = float('nan')

In [51]: a
Out[51]: inf

In [52]: b
Out[52]: -inf

In [53]: c
Out[53]: nan

In [54]: import math

In [55]: math.isinf(a)
Out[55]: True

In [56]: math.isnan(c)
Out[56]: True

In [57]: a = float('inf')

In [58]: a + 45
Out[58]: inf

In [59]: a * 10
Out[59]: inf

In [60]: 10 / a
Out[60]: 0.0

In [61]: a = float('inf')

In [62]: a/a
Out[62]: nan

In [63]: b = float('-inf')

In [64]: a + b
Out[64]: nan

In [65]: c = float('nan')

In [66]: c + 23
Out[66]: nan

In [67]: c / 2
Out[67]: nan

In [68]: c * 2
Out[68]: nan

In [69]: math.sqrt(c)
Out[69]: nan

In [70]: c = float('nan')

In [71]: d = float('nan')

In [72]: c == d
Out[72]: False

In [73]: c is d
Out[73]: False
