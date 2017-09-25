In [14]: from datetime import datetime

In [15]: from pytz import timezone

In [16]: d = datetime(2012, 12, 21, 9, 30, 0)

In [17]: d
Out[17]: datetime.datetime(2012, 12, 21, 9, 30)

In [18]: print(d)
2012-12-21 09:30:00

In [19]: central = timezone('US/Central')

In [20]: loc_d = central.localize(d)

In [21]: print(loc_d)
2012-12-21 09:30:00-06:00

In [22]: bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))

In [23]: print(bang_d)
2012-12-21 21:00:00+05:30

In [24]: d = datetime(2013, 3, 10, 1, 45)

In [25]: loc_d = central.localize(d)

In [26]: print(loc_d)
2013-03-10 01:45:00-06:00

In [27]: from datetime import timedelta

In [28]: later = central.normalize(loc_d + timedelta(minutes=30))

In [29]: print(later)
2013-03-10 03:15:00-05:00

In [30]: print(loc_d)
2013-03-10 01:45:00-06:00

In [33]: import pytz

In [34]: utc_d = loc_d.astimezone(pytz.utc)

In [35]: print(utc_d)
2013-03-10 07:45:00+00:00

In [36]: later_utc = utc_d + timedelta(minutes=30)

In [37]: print(later_utc.astimezone(central))
2013-03-10 03:15:00-05:00

In [38]: pytz.country_timezones['IN']
Out[38]: ['Asia/Kolkata']
