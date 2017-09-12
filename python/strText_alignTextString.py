text = 'Hello World'
text.ljust(20)
text.rjust(20)
text.center(20)

text.rjust(20, '=')
text.center(20,'*')

format(text, '>20')
format(text, '<20')
format(text, '^20')

format(text, '=>20s')
format(text, '*^20s')

'{:>10s} {:>10s}'.format('Hello', 'World')

x = 1.2345
format(x, '>10')
format(x, '^10.2f')

//output
In [11]: text = 'Hello World'

In [12]: text.ljust(20)
Out[12]: 'Hello World         '

In [14]: text.rjust(20)
Out[14]: '         Hello World'

In [15]: text.center(20)
Out[15]: '    Hello World     '

In [16]: text.rjust(20, '=')
Out[16]: '=========Hello World'

In [17]: text.center(20,'*')
Out[17]: '****Hello World*****'

In [18]: format(text, '>20')
Out[18]: '         Hello World'

In [19]: format(text, '<20')
Out[19]: 'Hello World         '

In [20]: format(text, '^20')
Out[20]: '    Hello World     '

In [21]:
    ...: format(text, '=>20s')
Out[21]: '=========Hello World'

In [22]: format(text, '*^20s')
Out[22]: '****Hello World*****'

In [23]:
    ...: '{:>10s} {:>10s}'.format('Hello', 'World')
Out[23]: '     Hello      World'

In [24]: x = 1.2345

In [25]: format(x, '>10')
Out[25]: '    1.2345'

In [26]: format(x, '^10.2f')
Out[26]: '   1.23   '
