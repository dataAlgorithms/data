In [64]: x = 1234

In [65]: bin(x)
Out[65]: '0b10011010010'

In [66]: oct(x)
Out[66]: '0o2322'

In [67]: hex(x)
Out[67]: '0x4d2'

In [68]: format(x, 'b')
Out[68]: '10011010010'

In [69]: format(x, 'o')
Out[69]: '2322'

In [70]: format(x, 'x')
Out[70]: '4d2'

In [71]: x = -1234

In [72]: format(x, 'b')
Out[72]: '-10011010010'

In [73]: format(x, 'x')
Out[73]: '-4d2'

In [74]: x = -1234

In [75]: format(2**32 + x, 'b')
Out[75]: '11111111111111111111101100101110'

In [76]: format(2**32 + x, 'x')
Out[76]: 'fffffb2e'

In [77]: int('4d2', 16)
Out[77]: 1234

In [78]: int('10011010010', 2)
Out[78]: 1234

In [79]: import os

In [81]: os.chmod('ddd.txt', 0o755)
