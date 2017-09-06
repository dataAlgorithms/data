# list comprehension (only for not very larger list)
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
[n for n in mylist if n > 0]
[n for n in mylist if n < 0]

//output
In [22]: [n for n in mylist if n > 0]
Out[22]: [1, 4, 10, 2, 3]
In [24]: [n for n in mylist if n < 0]
Out[24]: [-5, -7, -1]

# generator expression (suit for both small and larger list)
pos = (n for n in mylist if n > 0)
for x in pos:
    print(x, end=' ')

//output
1 4 10 2 3

# input involve exception handling 
values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False 

ivals = list(filter(is_int, values))
print(ivals)

//output
In [28]: print(ivals)
['1', '2', '-3', '4', '5']

# transform
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
import math
[math.sqrt(n) for n in mylist if n > 0]

clip_neq = [n if n > 0 else 0 for n in mylist]
clip_pos = [n if n < 0 else 0 for n in mylist]

//output
In [30]: [math.sqrt(n) for n in mylist if n > 0]
Out[30]: [1.0, 2.0, 3.1622776601683795, 1.4142135623730951, 1.7320508075688772]

In [31]: clip_neq = [n if n > 0 else 0 for n in mylist]
In [32]: clip_pos = [n if n < 0 else 0 for n in mylist]

In [33]: clip_neq
Out[33]: [1, 4, 0, 10, 0, 2, 3, 0]

In [34]: clip_pos
Out[34]: [0, 0, -5, 0, -7, 0, 0, -1]

# compress
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

## -- End pasted text --
counts = [0, 3, 10, 4, 1, 7, 6, 1]
from itertools import compress
more5 = [n > 5 for n in counts]
print(more5)

//output
[False, False, True, False, False, True, True, False]

In [39]: list(compress(addresses, more5))
Out[39]: ['5800 E 58TH', '1060 W ADDISON', '4801 N BROADWAY']
