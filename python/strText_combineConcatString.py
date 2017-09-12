In [1]: parts = ['Is', 'Chicago', 'Not', 'Chicago?']

In [2]: ' '.join(parts)
Out[2]: 'Is Chicago Not Chicago?'

In [3]: ','.join(parts)
Out[3]: 'Is,Chicago,Not,Chicago?'

In [4]: ''.join(parts)
Out[4]: 'IsChicagoNotChicago?'

In [5]: a = 'Is Chicago'

In [6]: b = 'Not Chicago?'

In [7]: a + ' ' + b
Out[7]: 'Is Chicago Not Chicago?'

In [8]: print('{} {}'.format(a, b))
Is Chicago Not Chicago?

In [9]: print(a  + ' ' + b)
Is Chicago Not Chicago?

In [10]: a = 'Hello' 'World'

In [11]: a
Out[11]: 'HelloWorld'

In [12]: data = ['ACME', 50, 91.1]

In [13]: ','.join(str(d) for d in data)
Out[13]: 'ACME,50,91.1'

In [14]: a
Out[14]: 'HelloWorld'

In [15]: b
Out[15]: 'Not Chicago?'

In [16]: c
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-16-2cd6ee2c70b0> in <module>()
----> 1 c

NameError: name 'c' is not defined

In [17]: print(a, b, sep=':')
HelloWorld:Not Chicago?

In [18]: def sample():
    ...:     yield 'Is'
    ...:     yield 'Chicago'
    ...:     yield 'Not'
    ...:     yield 'Chicago?'
    ...:

In [19]: text = ''.join(sample())

In [20]: text
Out[20]: 'IsChicagoNotChicago?'

In [21]: for part in sample():
    ...:     print part
  File "<ipython-input-21-92357aebbc44>", line 2
    print part
             ^
SyntaxError: Missing parentheses in call to 'print'


In [22]: for part in sample():
    ...:     print(part)
    ...:
Is
Chicago
Not
Chicago?

In [23]: %paste
def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0

    yield ''.join(parts)

for part in combine(sample(), 5):
    print(part)

## -- End pasted text --
IsChicago
NotChicago?


In [24]: %paste
def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0

    yield ''.join(parts)

for part in combine(sample(), 10):
    print(part)

## -- End pasted text --
IsChicagoNot
Chicago?

In [25]: %paste
def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0

    yield ''.join(parts)

for part in combine(sample(), 50):
    print(part)

## -- End pasted text --
IsChicagoNotChicago?

In [26]:
