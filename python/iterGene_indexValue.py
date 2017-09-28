In [22]: my_list = ['a', 'b', 'c']

In [23]: for idx, val in enumerate(my_list):
    ...:     print(idx, val)
    ...:
0 a
1 b
2 c

In [24]: for idx, val in enumerate(my_list, 1):
    ...:     print(idx, val)
    ...:
1 a
2 b
3 c

In [31]: %paste
def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            print(fields)
            try:
                count = fields[0]
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno, e))

## -- End pasted text --

In [32]: parse_data('somefile')
['#111']
['#333']
['#444']
['12345', '1111']
['67890', '2222']
['java', '3333']
['python', '4444']
['js', '5555']
['python', '6666']
['#nihao']
['dfjkdjf']
['fjdkfjkd']
['#python']
['#fdjkf']
['dfjkdf']

In [33]: %paste
word_summary = defaultdict(list)

with open('somefile', 'r') as f:
    lines = f.readlines()

In [35]: %paste
from collections import defaultdict

word_summary = defaultdict(list)

with open('somefile', 'r') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    # Create a list of words in current line
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

## -- End pasted text --

In [36]: print(word_summary)
defaultdict(<class 'list'>, {'67890': [4], '#444': [2], '4444': [6], '12345': [3
], 'dfjkdjf': [10], 'js': [7], '3333': [5], 'python': [6, 8], 'dfjkdf': [14], '5
555': [7], '2222': [4], '#nihao': [9], 'java': [5], '1111': [3], '#111': [0], '#
333': [1], 'fjdkfjkd': [11], '#fdjkf': [13], '6666': [8], '#python': [12]})

In [37]: !more somefile
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

In [38]: data = [(1,2),(3,4),(5,6),(7,8)]

In [39]: for n,(x,y) in enumerate(data):
    ...:     print(n,(x,y))
    ...:
0 (1, 2)
1 (3, 4)
2 (5, 6)
3 (7, 8)

In [40]:
