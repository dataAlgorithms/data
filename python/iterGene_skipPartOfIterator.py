In [78]: !type somefile
#111
#333
#444
12345 1111
67890 2222
java 3333
python 4444
js 5555
python 6666
#nihao
dfjkdjf
fjdkfjkd
#python
#fdjkf
dfjkdf

In [79]: %paste
# Print all lines
with open('somefile') as f:
    for line in f:
        print(line, end='')

print("\r\n")

# Drop begin comment lines
from itertools import dropwhile
with open('somefile') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')

print("\r\n")

from itertools import islice
items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)

print("\r\n")

# Drop all comment lines
with open('somefile') as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line, end='')
## -- End pasted text --
#111
#333
#444
12345 1111
67890 2222
java 3333
python 4444
js 5555
python 6666
#nihao
dfjkdjf
fjdkfjkd
#python
#fdjkf
dfjkdf


12345 1111
67890 2222
java 3333
python 4444
js 5555
python 6666
#nihao
dfjkdjf
fjdkfjkd
#python
#fdjkf
dfjkdf


1
4
10
15


12345 1111
67890 2222
java 3333
python 4444
js 5555
python 6666
dfjkdjf
fjdkfjkd
dfjkdf
