In [1]: from datetime import datetime

In [2]: text = '2012-09-20'

In [3]: y = datetime.strptime(text, '%Y-%m-%d')

In [4]: z = datetime.now()

In [5]: diff = z - y

In [6]: diff
Out[6]: datetime.timedelta(1831, 35493, 644469)

In [7]: y
Out[7]: datetime.datetime(2012, 9, 20, 0, 0)

In [8]: z
Out[8]: datetime.datetime(2017, 9, 25, 9, 51, 33, 644469)

In [9]: nice_z = datetime.strftime(z, '%A %B %d, %Y')

In [10]: nice_z
Out[10]: 'Monday September 25, 2017'

In [12]: from datetime import datetime

In [13]: def parse_ymd(s):
    ...:     year_s, mon_s, day_s = s.plit('-')
    ...:     return datetime(int(year_s), int(mon_s), int(day_s))
