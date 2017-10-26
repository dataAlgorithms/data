In [3]: from tempfile import TemporaryFile

In [4]: with TemporaryFile('w+t') as f:
   ...:     f.write('hello world\n')
   ...:     f.write('testing\n')
   ...:     f.seek(0)
   ...:     data = f.read()
   ...:

In [5]: print(data)
hello world
testing


In [6]: f = TemporaryFile('w+t')

In [7]: f.write('nihao')
Out[7]: 5

In [8]: f.seek(0)
Out[8]: 0

In [9]: data = f.read()

In [10]: print(data)
nihao

In [11]: f.close()

In [14]: with TemporaryFile('w+t', encoding='utf-8') as f:
    ...:     f.write('Hello\n')
    ...:     f.seek(0)
    ...:     data = f.read()
    ...:
    ...:
    ...:

In [15]: print(data)
Hello


In [16]: from tempfile import NamedTemporaryFile

In [17]: with NamedTemporaryFile('w+t') as f:
    ...:     print('filename is:', f.name)
    ...:
filename is: C:\Users\PING~1.ZHO\AppData\Local\Temp\tmpydbxm1wi

In [18]: with NamedTemporaryFile('w+t', delete=False) as f:
    ...:     print('filename is:', f.name)
    ...:
    ...:
filename is: C:\Users\PING~1.ZHO\AppData\Local\Temp\tmpgz1uiu2h

In [19]: !more C:\Users\PING~1.ZHO\AppData\Local\Temp\tmpgz1uiu2h

In [20]: from tempfile import TemporaryDirectory

In [21]: with TemporaryDirectory() as dirname:
    ...:     print('dirname is:', dirname)
    ...:
dirname is: C:\Users\PING~1.ZHO\AppData\Local\Temp\tmpv3y09vps

In [22]: import tempfile

In [23]: tempfile.mkstemp()
Out[23]: (6, 'C:\\Users\\PING~1.ZHO\\AppData\\Local\\Temp\\tmpda54y87h')

In [24]: tempfile.mkdtemp()
Out[24]: 'C:\\Users\\PING~1.ZHO\\AppData\\Local\\Temp\\tmpmqt3z2s3'

In [25]: tempfile.gettempdir()
Out[25]: 'C:\\Users\\PING~1.ZHO\\AppData\\Local\\Temp'


In [29]: f = NamedTemporaryFile(prefix='mytemp', suffix='.txt', dir='.')

In [30]: f.name
Out[30]: 'D:\\Program Files\\Anaconda3\\Scripts\\mytemp0otgc_7w.txt'
