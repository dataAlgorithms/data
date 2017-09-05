rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))

print(rows_by_fname)
print(rows_by_uid)
print(rows_by_lfname)

## -- End pasted text --
[{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}, {'fname': 'Brian', 'lname': 'J
ones', 'uid': 1003}, {'fname': 'David', 'lname': 'Beazley', 'uid': 1002}, {'fnam
e': 'John', 'lname': 'Cleese', 'uid': 1001}]
[{'fname': 'John', 'lname': 'Cleese', 'uid': 1001}, {'fname': 'David', 'lname':
'Beazley', 'uid': 1002}, {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}, {'fn
ame': 'Big', 'lname': 'Jones', 'uid': 1004}]
[{'fname': 'David', 'lname': 'Beazley', 'uid': 1002}, {'fname': 'John', 'lname':
 'Cleese', 'uid': 1001}, {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}, {'fnam
e': 'Brian', 'lname': 'Jones', 'uid': 1003}]


rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))

print(rows_by_fname)
print(rows_by_lfname)

## -- End pasted text --
[{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}, {'fname': 'Brian', 'lname': 'J
ones', 'uid': 1003}, {'fname': 'David', 'lname': 'Beazley', 'uid': 1002}, {'fnam
e': 'John', 'lname': 'Cleese', 'uid': 1001}]
[{'fname': 'David', 'lname': 'Beazley', 'uid': 1002}, {'fname': 'John', 'lname':
 'Cleese', 'uid': 1001}, {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}, {'fnam
e': 'Brian', 'lname': 'Jones', 'uid': 1003}]


In [61]: min(rows, key=itemgetter('uid'))
Out[61]: {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}

In [62]: min(rows, key=lambda r: r['fname'])
Out[62]: {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}

In [63]: min(rows, key=lambda r: r['uid'])
Out[63]: {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}

In [64]: max(rows, key=itemgetter('uid'))
Out[64]: {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
