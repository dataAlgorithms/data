a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

from collections import ChainMap
c = ChainMap(a, b)

print(c['x'])
print(c['y'])
print(c['z'])
print(c)
print(len(c))
print(c.keys())
print(c.values())

//output
1
2
3
ChainMap({'z': 3, 'x': 1}, {'z': 4, 'y': 2})
3
KeysView(ChainMap({'z': 3, 'x': 1}, {'z': 4, 'y': 2}))
ValuesView(ChainMap({'z': 3, 'x': 1}, {'z': 4, 'y': 2}))

c['z'] = 10
c['w'] = 40

In [28]: c
Out[28]: ChainMap({'z': 10, 'x': 1, 'w': 40}, {'z': 4, 'y': 2})
In [29]: del c['x']
In [30]: a
Out[30]: {'w': 40, 'z': 10}

values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])

//output
ChainMap({'x': 3}, {'x': 2}, {'x': 1})
3

values = values.parents
print(values['x'])
values = values.parents
print(values['x'])
print(values)

//output
2
1
ChainMap({'x': 1})

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print(merged['x'])
print(merged['y'])
print(merged['z'])

//output
1
2
3

a['x'] = 13
print(merged['x'])

//output
1

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = ChainMap(a, b)
print(merged['x'])
a['x'] = 42
print(merged['x'])

//output
1
42



