In [15]: # Some byte data

In [16]: s = b'hello'

In [17]: import base64

In [18]: # Encode as Base64

In [19]: a = base64.b64encode(s)

In [20]: a
Out[20]: b'aGVsbG8='

In [21]: # Decode from Base64

In [22]: base64.b64decode(a)
Out[22]: b'hello'

In [23]: base64.b64decode(a).decode('ascii')
Out[23]: 'hello'

In [24]:
