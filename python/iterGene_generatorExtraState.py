from collections import deque

class Linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()

with open('somefile') as f:
    lines = Linehistory(f)
    for line in lines:
        if 'java' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')

## -- End pasted text --
1:12345 1111
2:67890 2222
3:java 3333

In [67]: !type somefile
12345 1111
67890 2222
java 3333
python 4444
js 5555
python 6666
In [68]: %paste
from collections import deque

class Linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()

with open('somefile') as f:
    lines = Linehistory(f)
    for line in lines:
        if 'js' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')

## -- End pasted text --
3:java 3333
4:python 4444
5:js 5555

In [69]: %paste
from collections import deque

class Linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()

with open('somefile') as f:
    lines = Linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')

## -- End pasted text --
2:67890 2222
3:java 3333
4:python 4444
4:python 4444
5:js 5555
6:python 6666
