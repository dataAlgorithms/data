dsAlgo_splitStingOnAnyMulDelimiter.py

line = 'asdf fjdk; afed, fjek,asdf,            foo'
import re
re.split(r'[;,\s]\s*', line)

//output
Out[1]: ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

fields = re.split(r'(;|,|\s)\s*', line)
fields

//output
Out[3]: ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']

values = fields[::2]
delimiters = fields[1::2] + ['']
values 
delimiters

//output
In [5]: values
Out[5]: ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

In [6]: delimiters
Out[6]: [' ', ';', ',', ',', ',', '']


''.join(v+d for v,d in zip(values, delimiters))

//output
Out[7]: 'asdf fjdk;afed,fjek,asdf,foo'

re.split(r'(?:,|;|\s)\s*', line)

//output
Out[8]: ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
