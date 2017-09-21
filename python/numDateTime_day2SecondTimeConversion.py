In [1]: from datetime import timedelta

In [2]: a = timedelta(days=2, hours=6)

In [3]: a
Out[3]: datetime.timedelta(2, 21600)

In [4]: b = timedelta(hours=4.5)

In [5]: b
Out[5]: datetime.timedelta(0, 16200)

In [6]: c = a + b

In [7]: c
Out[7]: datetime.timedelta(2, 37800)

In [8]: 16200/4.5
Out[8]: 3600.0

In [9]: c.days
Out[9]: 2

In [10]: c.seconds
Out[10]: 37800

In [11]: c.seconds/3600
Out[11]: 10.5

In [12]: c.total_seconds()/3600
Out[12]: 58.5

In [13]: from datetime import datetime

In [14]: a = datetime(2012, 9, 23)

In [15]: a
Out[15]: datetime.datetime(2012, 9, 23, 0, 0)

In [16]: print(a + timedelta(days=10))
2012-10-03 00:00:00

In [17]: b = datetime(2012, 12, 21)

In [18]: d = b - a

In [19]: d.days
Out[19]: 89

In [20]: now = datetime.today()

In [21]: print(now)
2017-09-21 09:57:26.040304

In [22]: print(now + timedelta(minutes=10))
2017-09-21 10:07:26.040304

In [23]: a = datetime(2012, 3, 1)

In [24]: b = datetime(2012, 2, 28)

In [25]: a - b
Out[25]: datetime.timedelta(2)

In [26]: (a - b).days
Out[26]: 2

In [27]: c = datetime(2013, 3, 1)

In [28]: d = datetime(2013, 2, 28)

In [29]: (c -d).days
Out[29]: 1

In [30]: a = datetime(2012, 9, 23)

In [31]: a + timedelta(months=1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-31-8ba71fa4f0e5> in <module>()
----> 1 a + timedelta(months=1)

TypeError: 'months' is an invalid keyword argument for this function

In [33]: from dateutil.relativedelta import relativedelta

In [34]: a + relativedelta(months=+1)
Out[34]: datetime.datetime(2012, 10, 23, 0, 0)

In [35]: a + relativedelta(months=+4)
Out[35]: datetime.datetime(2013, 1, 23, 0, 0)

In [36]: b = datetime(2012, 12, 21)

In [37]: d = b - a

In [38]: d
Out[38]: datetime.timedelta(89)

In [39]: d = relativedelta(b, a)

In [40]: d
Out[40]: relativedelta(months=+2, days=+28)

In [41]: d.months
Out[41]: 2

In [42]: d.days
Out[42]: 28
