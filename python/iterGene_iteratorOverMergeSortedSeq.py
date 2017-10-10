In [1]: import heapq

In [2]: a = [1, 4, 7, 10]

In [3]: b = [2, 5, 6, 11]

In [4]: for c in heapq.merge(a, b):
   ...:     print(c)
   ...:
1
2
4
5
6
7
10
11



import heapq

with open('sorted_file_1', 'rt') as file1, \
     open('sorted_file_2') 'rt' as file2, \
     open('merged_file', 'wt') as outf:

    for line in heapq.merge(file1, file2):
        outf.write(line)
