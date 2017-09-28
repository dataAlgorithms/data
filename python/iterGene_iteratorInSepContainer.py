In [61]: from itertools import chain

In [62]: a = [1, 2, 3, 4]

In [63]: b = ['x', 'y', 'z']

In [64]: for x in chain(a, b):
    ...:     print(x)
    ...:
1
2
3
4
x
y
z
