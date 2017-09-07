filename = 'spam.txt'
filename.endswith('.txt')
filename.startswith('file:')

//output
In [10]: filename.endswith('.txt')
Out[10]: True

In [11]: filename.startswith('file:')
Out[11]: False

url = 'http://www.python.org'
url.startswith('http:')

//output
Out[10]: True

import os
filenames = os.listdir('.')
[name for name in filenames if name.endswith(('.c', '.h', '.py'))]
any(name.endswith('.py') for name in filenames)

//output
In [23]: [name for name in filenames if name.endswith(('.c', '.h', '.py'))]
Out[23]: ['rtmpPlay.py']

In [24]: any(name.endswith('.py') for name in filenames)
Out[24]: True

from urlib.request import urlopen

def read_data(name):
    if name.startswith('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

choices = ['http:', 'ftp:']
url.startswith(tuple(choices))

//output
Out[25]: True

import re
url = 'http://www.python.org'
re.match('http:|https:|ftp:', url)

//outout
Out[27]: <_sre.SRE_Match object; span=(0, 5), match='http:'>
