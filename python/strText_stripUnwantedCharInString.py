import re

s = '        hello world  \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())

//output
hello world
hello world

        hello world

t = '-------------hello=============='
print(t.lstrip('-'))
print(t.strip('-='))

//output
hello==============
hello

s = '       hello              world \n'
s = s.strip()
print(s)
print(re.sub('\s+', ' ', s))

//output
hello              world
hello world

with open(filename) as f:
    lines = (line.strip() for line in f)
    for line in lines:
        pass
