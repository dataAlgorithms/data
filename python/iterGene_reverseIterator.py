In [39]: a = [1, 2, 3, 4]

In [40]: for x in reversed(a):
    ...:     print(x, end=' ')
    ...:
4 3 2 1

In [42]: !type somefile
12345 7777
67890 8888
In [43]: f = open('somefile')

In [44]: for line in reversed(list(f)):
    ...:     print(line, end=' ')
    ...:
67890 8888 12345 7777

In [45]: for line in reversed(list(f)):
    ...:     print(line)
    ...:
    ...:

In [46]: f.close()

In [47]: f = open('somefile')

In [48]: for line in reversed(list(f)):
    ...:     print(line)
    ...:
67890 8888
12345 7777


In [49]: %paste
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

## -- End pasted text --

In [50]: numIter = Countdown(10)

In [51]: for i in numIter:
    ...:     print(i, end=' ')
    ...:
10 9 8 7 6 5 4 3 2 1
In [52]: for i in reversed(numIter):
    ...:     print(i, end=' ')
    ...:
1 2 3 4 5 6 7 8 9 10
