In [46]: from datetime import datetime, timedelta

In [47]: weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
    ...: 'Friday', 'Saturday', 'Sunday']

In [48]: %paste
def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date

## -- End pasted text --

In [49]: datetime.today()
Out[49]: datetime.datetime(2017, 9, 21, 11, 11, 28, 549401)

In [50]: get_previous_byday('Monday')
Out[50]: datetime.datetime(2017, 9, 18, 11, 11, 40, 825103)

In [51]: get_previous_byday('Tuesday')
Out[51]: datetime.datetime(2017, 9, 19, 11, 11, 59, 839190)

In [52]: get_previous_byday('Friday')
Out[52]: datetime.datetime(2017, 9, 15, 11, 12, 7, 776644)

In [53]: get_previous_byday('Sunday', datetime(2017, 9, 21))
Out[53]: datetime.datetime(2017, 9, 17, 0, 0)

In [54]: from datetime import datetime


In [57]: from dateutil.relativedelta import relativedelta

In [58]: from dateutil.rrule import *

In [59]: d = datetime.now()

In [60]: d
Out[60]: datetime.datetime(2017, 9, 21, 11, 19, 51, 298156)

In [61]: print(d + relativedelta(weekday=FR))
2017-09-22 11:19:51.298156

In [62]: print(d + relativedelta(weekday=FR(-1)))
2017-09-15 11:19:51.298156
