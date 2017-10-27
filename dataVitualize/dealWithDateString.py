# date to string
In [1]: from datetime import datetime

In [2]: d = datetime.now()

In [3]: d.isoformat()
Out[3]: '2017-10-27T17:12:31.485000'

# string to date
In [5]: from dateutil import parser
In [7]: d = parser.parse('2015-09-15T21:48:50.746Z')
d:\Anaconda2\lib\site-packages\dateutil\parser.py:605: UnicodeWarning: Unicode e
qual comparison failed to convert both arguments to Unicode - interpreting them
as being unequal
  elif res.tzname and res.tzname in time.tzname:

In [8]: d
Out[8]: datetime.datetime(2015, 9, 15, 21, 48, 50, 746000, tzinfo=tzutc())
