In [1]: import os

In [2]: import mmap

In [3]: def memory_map(filename, access=mmap.ACCESS_WRITE):
   ...:     size = os.path.getsize(filename)
   ...:     fd = os.open(filename, os.O_RDWR)
   ...:     return mmap.mmap(fd, size, access=access)
   ...:

In [4]: size = 10000

In [5]: with open('data', 'wb') as f:
   ...:     f.seek(size-1)
   ...:     f.write(b'\x00')
   ...:

In [6]: m = memory_map('data')

In [7]: len(m)
Out[7]: 10000

In [8]: m[0:10]
Out[8]: b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

In [9]: m[0]
Out[9]: 0

In [10]: m[0:11] = b'Hello World'

In [11]: m.close()

In [12]: with open('data', 'rb') as f:
    ...:     print(f.read(11))
    ...:
b'Hello World'

In [13]: with memory_map('data') as m:
    ...:     print(len(m))
    ...:     print(m[0:10])
    ...:
10000
b'Hello Worl'

In [14]: m = memory_map('data')

In [15]: v = memoryview(m).cast('I')

In [16]: v[0] = 7

In [17]: m[0:4]
Out[17]: b'\x07\x00\x00\x00'

In [18]: m[0:4]  = b'\x07\x01\x00\x00'

In [19]: v[0]
Out[19]: 263

By default, the memory_map() function shown opens a file for both reading and writing.
 Any modifications made to the data are copied back to the original file. 

If read-only access is needed instead, supply mmap.ACCESS_READ for the access argument. For example:

m = memory_map(filename, mmap.ACCESS_READ)

If you intend to modify the data locally, but don’t want those changes written back to the original file, use mmap.ACCESS_COPY:

m = memory_map(filename, mmap.ACCESS_COPY)
