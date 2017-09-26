'''
Use StopIteration
'''
with open('/etc/passwd') as f:
    try:
        while True:
            line = next(f)
            pritn(line, end='')
    except StopIteration:
        pass


'''
Use break
'''
with open('/etc/passwd') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')
        
'''
Ipython prompt
'''
In [1]: items = [1, 2, 3]

In [2]: it = iter(items)

In [3]: next(it)
Out[3]: 1

In [4]: next(it)
Out[4]: 2

In [5]: next(it)
Out[5]: 3

In [6]: next(it)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-6-2cdb14c0d4d6> in <module>()
----> 1 next(it)

StopIteration:

In [7]:
        
        
