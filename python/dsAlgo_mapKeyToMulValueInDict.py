d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}

In [3]: d
Out[3]: {'a': [1, 2, 3], 'b': [4, 5]}
In [4]: e
Out[4]: {'a': {1, 2, 3}, 'b': {4, 5}}

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['b'].append(4)
d['b'].append(5)

In [8]: d
Out[8]: defaultdict(list, {'a': [1, 2, 3], 'b': [4, 5]})

d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('a', []).append(4)

In [10]: d
Out[10]: {'a': [1, 2, 4]}

paris = (('a', 1), ('a', 2), ('a', 3))
d = defaultdict(list)
for key, value in paris:
    d[key].append(value)

In [12]: d
Out[12]: defaultdict(list, {'a': [1, 2, 3]})
