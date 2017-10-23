1. use io
In [17]: from io import BytesIO

In [18]: BytesIO().write(b'Hello')
Out[18]: 5

2. use sys
sys.stdout.buffer.write(b'Hello\n') (not work for me)

3. use "wb"
with open('myfile.txt', 'wb') as w:
    w.write(b'hello')
