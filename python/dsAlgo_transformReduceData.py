# Sum all item in a list
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)

//output
55

# Determine if any .py files exits in a directory
import os
files = os.listdir('.')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

//output
Sorry, no python.

# Output a tuple as csv
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

//output
ACME,50,123.45

portfolio = [
   {'name':'GOOG', 'shares': 50},
   {'name':'YHOO', 'shares': 75},
   {'name':'AOL', 'shares': 20},
   {'name':'SCOX', 'shares': 65}
]

min_shares = min(s['shares'] for s in portfolio)
print(min_shares)

//output
20

s = sum((x * x for x in nums))
print(s)
s = sum(x * x for x in nums)
print(s)

nums = [1, 2, 3, 4, 5]
s = sum([x * x for x in nums])
print(s)

//output
55
55
55

min_shares = min(s['shares'] for s in portfolio)
print(min_shares)

min_shares = min(portfolio, key=lambda s: s['shares'])
print(min_shares)

//output
20
{'name': 'AOL', 'shares': 20}
