In [20]: import os

In [21]: path = '/Users/beazley/Data/data.csv'

In [22]: os.path.basename(path)
Out[22]: 'data.csv'

In [23]: os.path.dirname(path)
Out[23]: '/Users/beazley/Data'

In [24]: os.path.join('tmp', 'data', os.path.basename(path))
Out[24]: 'tmp\\data\\data.csv'

In [25]: path = '~/Data/data.csv'

In [26]: os.path.expanduser(path)
Out[26]: 'C:\\Users\\ping.zhou/Data/data.csv'

In [28]: os.path.splitext(path)
Out[28]: ('~/Data/data', '.csv')
