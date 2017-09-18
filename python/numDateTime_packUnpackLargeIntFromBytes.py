In [1]: data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

In [2]: len(data)
Out[2]: 16

In [3]: int.from_bytes(data, 'little')
Out[3]: 69120565665751139577663547927094891008

In [4]: int.from_bytes(data, 'big')
Out[4]: 94522842520747284487117727783387188

In [5]: x = 94522842520747284487117727783387188

In [6]: x.to_bytes(16, 'big')
Out[6]: b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

In [7]: x.to_bytes(16, 'little')
Out[7]: b'4\x00#\x00\x01\xef\xcd\x00\xab\x90x\x00V4\x12\x00'

In [8]: data
Out[8]: b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

In [9]: import struct

In [10]: hi, lo = struct.unpack('>QQ', data)

In [11]: (hi << 64) + lo
Out[11]: 94522842520747284487117727783387188

In [12]: x = 0x01020304

In [13]: x.to_bytes(4, 'big')
Out[13]: b'\x01\x02\x03\x04'

In [14]: x.to_bytes(4, 'little')
Out[14]: b'\x04\x03\x02\x01'

In [15]: x = 523 ** 23

In [16]: x
Out[16]: 335381300113661875107536852714019056160355655333978849017944067

In [17]: x.to_bytes(16, 'little')
---------------------------------------------------------------------------
OverflowError                             Traceback (most recent call last)
<ipython-input-17-dcbe82b381e5> in <module>()
----> 1 x.to_bytes(16, 'little')

OverflowError: int too big to convert

In [18]: x.bit_length()
Out[18]: 208

In [19]: nbytes, rem = divmod(x.bit_length(), 8)

In [20]: if rem:
    ...:     nbytes += 1
    ...:

In [21]: x.to_bytes(nbytes, 'little')
Out[21]: b'\x03X\xf1\x82iT\x96\xac\xc7c\x16\xf3\xb9\xcf\x18\xee\xec\x91\xd1\x98\
xa2\xc8\xd9R\xb5\xd0'
