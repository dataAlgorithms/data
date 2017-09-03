In [36]: record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
In [38]: name, email, *phone_numbers = record
In [39]: name
Out[39]: 'Dave'
In [40]: email
Out[40]: 'dave@example.com'
In [41]: phone_numbers
Out[41]: ['773-555-1212', '847-555-1212']

In [45]: *trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
In [46]: trailing
Out[46]: [10, 8, 7, 1, 9, 5, 10]
In [47]: current
Out[47]: 3

In [49]: records = [
    ...:     ('foo', 1, 2),
    ...:     ('bar', 'hello'),
    ...:     ('foo', 3, 4),
    ...: ]
In [50]: def do_foo(x, y):
    ...:     print('foo', x, y)
    ...:
In [51]: def do_bar(s):
    ...:     print('bar', s)
    ...:
In [52]: for tag, *args in records:
    ...:     if tag == 'foo':
    ...:         do_foo(*args)
    ...:     elif tag == 'bar':
    ...:         do_bar(*args)
    ...:
foo 1 2
bar hello
foo 3 4

In [53]: line = 'nobody:*:-2:-2:Unprivileded User:/var/empty:/usr/bin/false'
In [54]: uname, *fields, homedir, sh = line.split(':')
In [55]: uname
Out[55]: 'nobody'
In [56]: homedir
Out[56]: '/var/empty'
In [57]: sh
Out[57]: '/usr/bin/false'
In [58]: fields
Out[58]: ['*', '-2', '-2', 'Unprivileded User']

In [59]: record = ('ACME', 50, 123,45, (12, 18, 2012))
In [60]: name, *_, (*_, year) = record
In [61]: name
Out[61]: 'ACME'
In [62]: year
Out[62]: 2012

In [63]: items = [1, 10, 7, 4, 5, 9]
In [64]: head, *tail = items
In [65]: head
Out[65]: 1
In [66]: tail
Out[66]: [10, 7, 4, 5, 9]

In [67]: def sum(items):
    ...:     head, *tail = items
    ...:     return head + sum(tail) if tail else head
    ...:

In [68]: sum(items)
Out[68]: 36
