In [8]: import io

In [9]: s = io.StringIO()

In [10]: s.write('Hello World\n')
Out[10]: 12

In [11]: print('This is a test', file=s)

In [12]: s.getvalue()
Out[12]: 'Hello World\nThis is a test\n'

In [13]: s = io.StringIO('Hello\nWorld\n')

In [14]: s.read(4)
Out[14]: 'Hell'

In [15]: s.read()
Out[15]: 'o\nWorld\n'

In [16]: s = io.BytesIO()

In [17]: s.write(b'binary data')
Out[17]: 11

In [18]: s.getvalue()
Out[18]: b'binary data'
