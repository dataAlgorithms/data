In [1]: %paste
def add(x:int, y:int) -> int:
    return x + y
## -- End pasted text --

In [2]: help(add)
Help on function add in module __main__:

add(x:int, y:int) -> int


In [3]: add.__annotations__
Out[3]: {'return': int, 'x': int, 'y': int}
