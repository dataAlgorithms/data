In [70]: def count(n):
    ...:     while True:
    ...:         yield n
    ...:         n += 1
    ...:

In [71]: c = count(0)

In [72]: c[10:20]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-72-f37106ac0c7d> in <module>()
----> 1 c[10:20]

TypeError: 'generator' object is not subscriptable

In [73]: import itertools

In [74]: for x in itertools.islice(c, 10, 20):
    ...:     print(x, end=' ')
    ...:
10 11 12 13 14 15 16 17 18 19
In [75]:
