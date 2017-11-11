In [1]: # Initial byte string

In [2]: s = b'hello'

In [3]: # encode as hex

In [4]: import binascii

In [5]: h = binascii.b2a_hex(s)

In [6]: h
Out[6]: b'68656c6c6f'

In [8]: # decode back to bytes

In [9]: binascii.a2b_hex(h)
Out[9]: b'hello'

In [10]: import base64

In [11]: h = base64.b16encode(s)   #upper output hex

In [12]: h
Out[12]: b'68656C6C6F'

In [13]: base64.b16decode(h)
Out[13]: b'hello'

In [14]: h.decode('ascii')
Out[14]: '68656C6C6F'

In [15]:
