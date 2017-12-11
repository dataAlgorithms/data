In [13]: add = lambda x, y: x + y

In [14]: add(2, 3)
Out[14]: 5

In [15]: add('hello', 'world')
Out[15]: 'helloworld'

In [16]: names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Bat
    ...: chelder']

In [17]: sorted(names, key=lambda name: name.split()[-1].lower())
Out[17]: ['Ned Batchelder', 'David Beazley', 'Raymond Hettinger', 'Brian Jones']
