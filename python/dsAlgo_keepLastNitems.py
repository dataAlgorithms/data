from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

with open('somefile.txt') as f:

    for line ,prevlines in search(f, 'python', 500):
        for pline in prevlines:
            print(pline, end='')
        print('0000000000000')
        print(line, end='')
        print('-' * 20)

'''
cat somefile.txt
111111111 python
222222222 java
333333333 python

output:
0000000000000
111111111 python
--------------------
111111111 python
222222222 java
0000000000000
333333333 python
---------------------
'''

In [17]: q = deque(maxlen=3)
In [18]: q.append(1)
In [19]: q.append(2)
In [20]: q.append(3)
In [21]: q
Out[21]: deque([1, 2, 3])
In [22]: q.append(4)
In [23]: q
Out[23]: deque([2, 3, 4])
In [24]: q.append(5)
In [25]: q
Out[25]: deque([3, 4, 5])

In [26]: q = deque()
In [27]: q.append(1)
In [28]: q.append(2)
In [29]: q.append(3)
In [30]: q
Out[30]: deque([1, 2, 3])
In [31]: q.appendleft(4)
In [32]:
In [32]: q
Out[32]: deque([4, 1, 2, 3])
In [33]: q.pop()
Out[33]: 3
In [34]: q
Out[34]: deque([4, 1, 2])
In [35]: q.popleft()
Out[35]: 4
In [36]: q
Out[36]: deque([1, 2])
In [37]:
