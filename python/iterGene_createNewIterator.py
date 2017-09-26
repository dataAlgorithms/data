def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

for n in frange(0, 4, 0.5):
    print(n)

//output
0
0.5
1.0
1.5
2.0
2.5
3.0
3.5

print(list(frange(0, 1, 0.125)))

//output
[0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875]

def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')

c = countdown(3)
c
next(c)
next(c)
next(c)
next(c)

//output
Out[11]: <generator object countdown at 0x0000000005CFCE60>

In [12]: next(c)
Starting to count from 3
Out[12]: 3

In [13]: next(c)
Out[13]: 2

In [14]: next(c)
Out[14]: 1

In [15]: next(c)
Done!
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-15-73b012f9653f> in <module>()
----> 1 next(c)

StopIteration:

In [16]:


