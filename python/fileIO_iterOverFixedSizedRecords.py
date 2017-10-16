In [3]: !more somefile.txt
111111
222222
333333
444444
555555
666666

In [4]: from functools import partial

In [5]: with open('somefile.txt', 'rb') as f:
   ...:     records = iter(partial(f.read, 3), b'')
   ...:     for r in records:
   ...:         print(r)
   ...:
b'111'
b'111'
b'\r\n2'
b'222'
b'22\r'
b'\n33'
b'333'
b'3\r\n'
b'444'
b'444'
b'\r\n5'
b'555'
b'55\r'
b'\n66'
b'666'
b'6\r\n'
