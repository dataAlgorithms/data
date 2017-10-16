In [1]: import os.path

In [2]: os.path
Out[2]: <module 'ntpath' from 'D:\\Program Files\\Anaconda3\\lib\\ntpath.py'>

In [3]: def read_into_buffer(filename):
   ...:     buf = bytearray(os.path.getsize(filename))
   ...:     with open(filename, 'rb') as f:
   ...:         f.readinto(buf)
   ...:     return buf
   ...:

In [4]: with open('sample.bin', 'wb') as f:
   ...:     f.write(b'Hello World')
   ...:

In [5]: buf = read_into_buffer('sample.bin')

In [6]: buf
Out[6]: bytearray(b'Hello World')

In [7]: buf[0:5] = b'Hallo'

In [8]: buf
Out[8]: bytearray(b'Hallo World')

In [9]: with open('newsmaple.bin', 'wb') as f:
   ...:     f.write(buf)
   ...:

In [10]: !more newsmaple.bin
Hallo World

In [11]: buf
Out[11]: bytearray(b'Hallo World')

In [12]: m1 = memoryview(buf)

In [13]: m1
Out[13]: <memory at 0x0000000004C39348>

In [14]: m2 = m1[-5:]

In [15]: m2
Out[15]: <memory at 0x0000000004C39408>

In [16]: m2[:] = b'WORLD'

In [17]: buf
Out[17]: bytearray(b'Hallo WORLD')

In [18]:
