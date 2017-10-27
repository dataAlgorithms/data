import pickle

class Hello:
    def __init__(self):
        print("Hello")

print("\r\n::Dump object to a file")
data = Hello()
f = open('somefile', 'wb')
pickle.dump(data, f)
f.close()

print("\r\n::Dump object to a string")
s = pickle.dumps(data)
print(s)

print("\r\n::Restore from a file")
f = open('somefile', 'rb')
data = pickle.load(f)
print(data)

print('\r\n::Restore from a string')
data = pickle.loads(s)
print(data)

print('\r\n::Pickle functions, class, instace')
import math
import pickle
pickle.dumps(math.cos)
data = pickle.loads(s)
print(data)

'''
::Dump object to a file
Hello

::Dump object to a string
b'\x80\x03c__main__\nHello\nq\x00)\x81q\x01.'

::Restore from a file
<__main__.Hello object at 0x0000000004D410B8>

::Restore from a string
<__main__.Hello object at 0x0000000004D41048>

::Pickle functions, class, instace
<__main__.Hello object at 0x0000000004D41080>
'''
