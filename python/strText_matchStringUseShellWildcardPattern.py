from fnmatch import fnmatch, fnmatchcase

fnmatch('foo.txt', '*.txt')
fnmatch('foo.txt', '?oo.txt')
fnmatch('Dat45.csv', 'Dat[0-9]*')

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
[name for name in names if fnmatch(name, 'Dat*.csv')]

fnmatchcase('foo.txt', '*.TXT')

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

[addr for addr in addresses if fnmatchcase(addr, '* ST')]
[addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]

//output
In [30]: fnmatch('foo.txt', '*.txt')
Out[30]: True

In [31]: fnmatch('foo.txt', '?oo.txt')
Out[31]: True

In [32]: fnmatch('Dat45.csv', 'Dat[0-9]*')
Out[32]: True

In [33]: names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']

In [34]: [name for name in names if fnmatch(name, 'Dat*.csv')]
Out[34]: ['Dat1.csv', 'Dat2.csv']

In [35]: fnmatchcase('foo.txt', '*.TXT')
Out[35]: False

In [36]: %paste
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]
## -- End pasted text --

In [37]:
    ...: [addr for addr in addresses if fnmatchcase(addr, '* ST')]
Out[37]: ['5412 N CLARK ST', '1060 W ADDISON ST', '2122 N CLARK ST']

In [38]: [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*
    ...: ')]
Out[38]: ['5412 N CLARK ST']
