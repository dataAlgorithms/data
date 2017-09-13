In [1]: s = '{name} has {n} messages.'

In [2]: s.format(naem='Guido', n=37)
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-2-b50cc29cde2a> in <module>()
----> 1 s.format(naem='Guido', n=37)

KeyError: 'name'

In [3]: s.format(name='Guido', n=37)
Out[3]: 'Guido has 37 messages.'

In [4]: name = 'Guido'

In [5]: n = 37

In [6]: s.format_map(vars())
Out[6]: 'Guido has 37 messages.'

In [7]: class Info:
   ...:     def __init__(self, name, n):
   ...:         self.name = name
   ...:         self.n = n
   ...:

In [8]: a = Info('Guido', 37)

In [9]: s.format_map(vars(a))
Out[9]: 'Guido has 37 messages.'

In [10]: s.format(name='Guido')
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-10-dac1742a40f0> in <module>()
----> 1 s.format(name='Guido')

KeyError: 'n'

In [11]: class safesub(dict):
    ...:     def __missing__(self, key):
    ...:         return '{' + key + '}'
    ...:

In [12]: del n

In [14]: s.format_map(safesub(vars()))
Out[14]: 'Guido has {n} messages.'

In [15]: import sys

In [16]: def sub(text):
    ...:     return text.format_map(safesub(sys._getframe(1).f_locals))
    ...:

In [17]: name = 'Guido'

In [18]: n = 37

In [19]: print(sub('Hello {name}'))
Hello Guido

In [20]: print(sub('You have {n} messages.'))
You have 37 messages.

In [21]: print(sub('Your favorite color is {color}'))
Your favorite color is {color}


In [25]: name = 'Guido'

In [26]: n = 37

In [27]: '%(name) has %(n) messages.' % vars()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-27-81a1f6a35737> in <module>()
----> 1 '%(name) has %(n) messages.' % vars()

ValueError: unsupported format character 'm' (0x6d) at index 17

In [28]: import string

In [29]: s = string.Template('$name has $n messages.')


In [31]: s.substitute(vars())
Out[31]: 'Guido has 37 messages.'
