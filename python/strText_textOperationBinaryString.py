data = b'Hello World'

print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

//output
Hello
True
['Hello', 'World']
Hello Cruel World

data = bytearray(b'hello world')
print(data[0:5])
print(data.startswith(b'hello'))
print(data.split())
print(data.replace(b'hello', b'Hello cruel'))

//output
hello
True
[bytearray(b'hello'), bytearray(b'world')]
Hello cruel world

data = b'FOO:BAR,SPAM'
import re
print(re.split(b'[:,]', data))

//output
['FOO', 'BAR', 'SPAM']

a = 'Hello world'
print(a[0])

b = b'hello world'
print(b[0])

s = b'hello world'
print(s)
print(s.decode('ascii'))


print('{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii'))

//output
H
h
hello world
hello world
ACME              100     490.10

import os
print(os.listdir('.'))
print(os.listdir(b'.'))

//output
['1.txt', 'Application.tar.gz', 'chn-sms-set.sh', 'tmp', 'zzz.tzr (2).gz', 'zzz.
tzr.gz']
['1.txt', 'Application.tar.gz', 'chn-sms-set.sh', 'tmp', 'zzz.tzr (2).gz', 'zzz.
tzr.gz']
