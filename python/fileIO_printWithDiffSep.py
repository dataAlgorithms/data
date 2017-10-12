In [1]: print('ACME', 50, 91.5)
ACME 50 91.5

In [2]: print('ACME', 50, 91.5, sep=',')
ACME,50,91.5

In [3]: print('ACME', 50, 91.5, sep=',', end='!!\n')
ACME,50,91.5!!

In [4]: for i in range(5):
   ...:     print(i)
   ...:
0
1
2
3
4

In [5]: for i in range(5):
   ...:     print(i, end=' ')
   ...:
0 1 2 3 4

In [10]: ','.join(('ACME', '50'))
Out[10]: 'ACME,50'

In [11]: print(','.join(('ACME','50','91.5')))
ACME,50,91.5

In [12]: row = ('ACME', 50, 91.5)


In [14]: print(','.join(str(x) for x in row))
ACME,50,91.5

In [15]: print(*row, sep=',')
ACME,50,91.5
