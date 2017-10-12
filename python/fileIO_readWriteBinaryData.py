In [16]: !more somefile.txt
111111
222222
333333
444444
555555
666666

In [17]: # Read the entire file as a single byte string

In [18]: with open('somefile.txt', 'rb') as f:
    ...:     data = f.read()
    ...:

In [19]: print(data)
b'111111\r\n222222\r\n333333\r\n444444\r\n555555\r\n666666\r\n'

In [20]: # Write binary data to a file

In [21]: with open('somefile.bin', 'wb') as f:
    ...:     f.write(b'Hello World')
    ...:

In [22]: !more somefile.bin
Hello World

In [23]: t = 'Hello world'

In [24]: t[0]
Out[24]: 'H'

In [25]: for c in t:
    ...:     print(c)
    ...:
H
e
l
l
o

w
o
r
l
d

In [26]: b = b'Hello world'

In [27]: b[0]
Out[27]: 72

In [28]: for c in b:
    ...:     print(c)
    ...:
72
101
108
108
111
32
119
111
114
108
100

In [29]: with open('somefile.bin', 'rb') as f:
    ...:     data = f.read(16)
    ...:     text = data.decode('utf-8')
    ...:

In [30]: print(data)
b'Hello World'

In [31]: print(text)
Hello World

In [32]: with open('somefile.bin', 'wb') as f:
    ...:     text = 'Hello world'
    ...:     f.write(text.encode('utf-8'))
    ...:

In [33]: !more somefile.bin
Hello world

In [34]: import array

In [35]: nums = array.array('i', [1, 2, 3, 4])

In [36]: with open('data.bin', 'wb') as f:
    ...:     f.write(nums)
    ...:

In [37]: !more data.bin













In [38]: import array

In [39]: a = array.array('i', [0, 0, 0, 0, 0, 0, 0])

In [40]: with open('data.bin', 'rb') as f:
    ...:     f.readinto(a)
    ...:

In [41]: a
Out[41]: array('i', [1, 2, 3, 4, 0, 0, 0])

In [42]:
