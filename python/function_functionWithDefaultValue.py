In [8]: %paste
_no_value = object()

def spam(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')

## -- End pasted text --

In [9]: spam(1)
No b value supplied

In [10]: spam(1, 2)

In [11]: spam(1, None)
