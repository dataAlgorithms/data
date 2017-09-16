In [44]: x = 1234.56789

In [45]: format(x, '0.2f')
Out[45]: '1234.57'

In [46]: format(x, '>10.1f')
Out[46]: '    1234.6'

In [47]: format(x, '<10.1f')
Out[47]: '1234.6    '

In [48]: format(x, '^10.1f')
Out[48]: '  1234.6  '

In [49]: format(x, ',')
Out[49]: '1,234.56789'

In [50]: format(x,'0,.1f')
Out[50]: '1,234.6'

In [51]: format(x, 'e')
Out[51]: '1.234568e+03'

In [52]: format(x, '0.2E')
Out[52]: '1.23E+03'

In [53]: 'The value is {:0,.2f}'.format(x)
Out[53]: 'The value is 1,234.57'

In [54]: x
Out[54]: 1234.56789

In [55]: format(x, '0.1f')
Out[55]: '1234.6'

In [56]: format(-x, '0.1f')
Out[56]: '-1234.6'

In [57]: swap_sep = {ord('.'):',', ord(','):'.'}

In [58]: format(x, ',').translate(swap_sep)
Out[58]: '1.234,56789'

In [59]: '%0.2f' % x
Out[59]: '1234.57'

In [60]: '%10.1f' % x
Out[60]: '    1234.6'

In [61]: '%-10.1f' % x
Out[61]: '1234.6    '

In [62]:
