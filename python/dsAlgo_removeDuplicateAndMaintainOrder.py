# remove duplicate, but the order is changed
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(a)
print(set(a)) # order is changed

# remove duplicate, and order is maintained, but only suit for hash sequence
def dedupeHash(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupeHash(a)))

# remove duplicate, and order is maintained, suit for hash and non-hash sequence
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [{'x':1, 'y': 2}, {'x': 1, 'y':3}, {'x': 1,  'y':2}, {'x': 2,  'y':4}]
print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))
print(list(dedupe(a, key=lambda d: d['x'])))

'''
[1, 5, 2, 1, 9, 1, 5, 10]
{1, 2, 10, 5, 9}
[1, 5, 2, 9, 10]
[{'y': 2, 'x': 1}, {'y': 3, 'x': 1}, {'y': 4, 'x': 2}]
[{'y': 2, 'x': 1}, {'y': 4, 'x': 2}]
'''

# remove duplicate for file
with open('somefile.txt', 'r') as f:
    for line in dedupe(f):
        print(line)

'''
[root@RND-SM-1-59Q code]# cat somefile.txt 
1111 java
2222 python
1111 java
3333 scala
4444 java
4444 java
5555 python

[root@RND-SM-1-59Q code]# python a.py 
1111 java
2222 python
3333 scala
4444 java
5555 python
'''
