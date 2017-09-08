text = 'yeah, but no, but yeah, but no, but yeah'
text.replace('yeah', 'yep')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)

import re
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
datepat.sub(r'\3-\1-\2', text)

from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

datepat.sub(change_date, text)

newtext, n = datepat.subn(r'\3-\1-\2', text)
newtext
n

//output
In [67]: text = 'yeah, but no, but yeah, but no, but yeah'

In [68]: text.replace('yeah', 'yep')
Out[68]: 'yep, but no, but yep, but no, but yep'

In [69]: text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    ...: import re
    ...: re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
    ...:
Out[69]: 'Today is 2012-11-27. PyCon starts 2013-3-13.'

In [70]: import re
    ...: datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    ...: datepat.sub(r'\3-\1-\2', text)
    ...:
Out[70]: 'Today is 2012-11-27. PyCon starts 2013-3-13.'

In [71]: from calendar import month_abbr
    ...: def change_date(m):
    ...:     mon_name = month_abbr[int(m.group(1))]
    ...:     return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
    ...:
    ...: datepat.sub(change_date, text)
    ...:
Out[71]: 'Today is 27 Nov 2012. PyCon starts 13 Mar 2013.'

In [72]: newtext, n = datepat.subn(r'\3-\1-\2', text)

In [73]: newtext
Out[73]: 'Today is 2012-11-27. PyCon starts 2013-3-13.'

In [74]: n
Out[74]: 2
