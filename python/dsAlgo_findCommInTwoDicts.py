a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# Find keys in common
keyComm = a.keys() & b.keys()
print(keyComm)

# Find keys in a that are not in b
keyNot = a.keys() - b.keys()
print(keyNot)

# Find (key, value) pairs in common
itemComm = a.items() & b.items()
print(itemComm)

# Make a new dictionary with certail keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c)

## -- End pasted text --
{'y', 'x'}
{'z'}
{('y', 2)}
{'y': 2, 'x': 1}
