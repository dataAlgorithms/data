In [1]: items = ['a', 'b', 'c']

In [2]: from itertools import permutations

In [3]: for p in permutations(items):
   ...:     print(p)
   ...:
('a', 'b', 'c')
('a', 'c', 'b')
('b', 'a', 'c')
('b', 'c', 'a')
('c', 'a', 'b')
('c', 'b', 'a')

In [5]: for p in permutations(items, 2):
   ...:     print(p)
   ...:
   ...:
('a', 'b')
('a', 'c')
('b', 'a')
('b', 'c')
('c', 'a')
('c', 'b')

In [6]: from itertools import combinations

In [7]: for c in combinations(items, 3):
   ...:     print(c)
   ...:
('a', 'b', 'c')

In [8]: for c in combinations(items, 2):
   ...:     print(c)
   ...:
('a', 'b')
('a', 'c')
('b', 'c')

In [9]: for c in combinations(items, 1):
   ...:     print(c)
   ...:
('a',)
('b',)
('c',)

In [12]: from itertools import combinations_with_replacement

In [13]: for c in combinations_with_replacement(items, 3):
    ...:     print(c)
    ...:
    ...:
('a', 'a', 'a')
('a', 'a', 'b')
('a', 'a', 'c')
('a', 'b', 'b')
('a', 'b', 'c')
('a', 'c', 'c')
('b', 'b', 'b')
('b', 'b', 'c')
('b', 'c', 'c')
('c', 'c', 'c')

In [14]:
