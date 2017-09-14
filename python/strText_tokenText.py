text = 'foo = 23 + 42 * 18'

tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
      ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]

import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME,NUM,PLUS,TIMES,EQ,WS]))

scanner = master_pat.scanner('foo = 42')
scanner.match()
_.lastgroup, _.group()
scanner.match()
_.lastgroup, _.group()
scanner.match()
_.lastgroup, _.group()
scanner.match()
_.lastgroup, _.group()
scanner.match()
_.lastgroup, _.group()
scanner.match()
_.lastgroup, _.group()

from collections import namedtuple

Token = namedtuple('Token', ['type', 'value'])

def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())

for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)

tokens = (tok for tok in generate_tokens(master_pat, text)
            if tok.type != 'WS')
for tok in tokens:
    print(tok)

LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'

master_pat = re.compile('|'.join([LE, LT, EQ]))
PRINT = r'(?P<PRINT>print)'
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'

master_pat = re.compile('|'.join([PRINT, NAME]))

for tok in generate_tokens(master_pat, 'printer'):
    print(tok)

//output
text = 'foo = 23 + 42 * 18'

tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
      ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]

import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME,NUM,PLUS,TIMES,EQ,WS]))

## -- End pasted text --

In [7]:
   ...: scanner = master_pat.scanner('foo = 42')

In [8]: scanner.match()
Out[8]: <_sre.SRE_Match object; span=(0, 3), match='foo'>

In [9]: _.lastgroup, _.group()
Out[9]: ('NAME', 'foo')

In [10]: scanner.match()
Out[10]: <_sre.SRE_Match object; span=(3, 4), match=' '>

In [11]: _.lastgroup, _.group()
Out[11]: ('WS', ' ')

In [12]: scanner.match()
Out[12]: <_sre.SRE_Match object; span=(4, 5), match='='>

In [13]: _.lastgroup, _.group()
Out[13]: ('EQ', '=')

In [14]: scanner.match()
Out[14]: <_sre.SRE_Match object; span=(5, 6), match=' '>

In [15]: _.lastgroup, _.group()
Out[15]: ('WS', ' ')

In [16]: scanner.match()
Out[16]: <_sre.SRE_Match object; span=(6, 8), match='42'>

In [17]: _.lastgroup, _.group()
Out[17]: ('NUM', '42')

In [18]: scanner.match()

In [20]: %paste
from collections import namedtuple

Token = namedtuple('Token', ['type', 'value'])

def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())

for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)

## -- End pasted text --
Token(type='NAME', value='foo')
Token(type='WS', value=' ')
Token(type='EQ', value='=')
Token(type='WS', value=' ')
Token(type='NUM', value='42')

In [21]: %paste

tokens = (tok for tok in generate_tokens(master_pat, text)
            if tok.type != 'WS')
for tok in tokens:
    print(tok)

## -- End pasted text --
Token(type='NAME', value='foo')
Token(type='EQ', value='=')
Token(type='NUM', value='23')
Token(type='PLUS', value='+')
Token(type='NUM', value='42')
Token(type='TIMES', value='*')
Token(type='NUM', value='18')

In [22]: %paste
LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'

master_pat = re.compile('|'.join([LE, LT, EQ]))
PRINT = r'(?P<PRINT>print)'
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'

master_pat = re.compile('|'.join([PRINT, NAME]))

## -- End pasted text --

In [23]: %paste

for tok in generate_tokens(master_pat, 'printer'):
    print(tok)

## -- End pasted text --
Token(type='PRINT', value='print')
Token(type='NAME', value='er')
