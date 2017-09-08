text = 'yeah, but no, but yeah, but no, but yeah'

In [40]: text == 'yeah'
Out[40]: False
In [43]: text.startswith('yeah')
Out[43]: True
In [44]: text.endswith('no')
Out[44]: False

In [45]: text.find('no')
Out[45]: 10

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')

text = 'Tdoay is 11/27/2012, Python starts 3/13/2013'

In [53]: datepat.findall(text)
Out[53]: ['11/27/2012', '3/13/2013']

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
m
m.group(0)
m.group(1)
m.group(2)
m.group(3)
m.groups()
month, day, year = m.groups()

text
datapat.findall(text)
for month, day, year in datepat.findall(text):
    print("{}-{}-{}".format(year, month, day))

for m in datepat.finditer(text):
    print(m.groups())

//output
In [52]: text = 'Tdoay is 11/27/2012, Python starts 3/13/2013'
    ...: datepat.findall(text)
    ...:
Out[52]: ['11/27/2012', '3/13/2013']

In [53]: datepat.findall(text)
Out[53]: ['11/27/2012', '3/13/2013']

In [54]: datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    ...: m = datepat.match('11/27/2012')
    ...:

In [55]: m
Out[55]: <_sre.SRE_Match object; span=(0, 10), match='11/27/2012'>

In [56]: m.group(0)
Out[56]: '11/27/2012'

In [57]: m.group(1)
Out[57]: '11'

In [58]: m.group(2)
Out[58]: '27'

In [59]: m.group(3)
Out[59]: '2012'

In [60]: m.groups()
Out[60]: ('11', '27', '2012')

In [61]: month, day, year = m.groups()

In [62]: text
Out[62]: 'Tdoay is 11/27/2012, Python starts 3/13/2013'

In [64]: datepat.findall(text)
Out[64]: [('11', '27', '2012'), ('3', '13', '2013')]

In [65]: for month, day, year in datepat.findall(text):
    ...:     print("{}-{}-{}".format(year, month, day))
    ...:
2012-11-27
2013-3-13

In [66]: for m in datepat.finditer(text):
    ...:     print(m.groups())
    ...:
('11', '27', '2012')
('3', '13', '2013')
