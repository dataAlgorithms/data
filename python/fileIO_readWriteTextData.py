In [34]: %paste
# Read the entire file as a single string
with open('somefile.txt', 'rt') as f:
    data = f.read()

## -- End pasted text --

In [35]: print(data)
111111
222222
333333
444444
555555
666666

In [37]: %paste
# Iterate over the lines of the file
with open('somefile.txt', 'rt') as f:
    for line in f:
        # process line
        print(line)

## -- End pasted text --
111111

222222

333333

444444

555555

666666

In [38]: %paste
# Write chunks of text data
with open('somefile1.txt', 'wt') as f:
    f.write('text1')
    f.write('text2')

!more somefile1.txt

## -- End pasted text --
text1text2
    
In [39]: %paste
# Redirected print statement
with open('somefile2.txt', 'wt') as f:
    print('line1', file=f)
    print('line2', file=f)

!more somefile2.txt
## -- End pasted text --
line1
line2

with open('somefile.txt', 'rt', encoding='latin-1') as f:
     pass

In [41]: f = open('somefile.txt', 'rt')
    ...: data = f.read()
    ...: f.close()
    ...:

In [42]: print(data)
111111
222222
333333
444444
555555
666666


In [22]: # Read with disabled newline translation

In [23]: with open('somefile.txt', 'rt', newline='') as f:
    ...:     data = f.read()
    ...:

In [24]: print(data)
111111
222222
333333
444444
555555
666666

>>> f = open('sample.txt', 'rt', encoding='ascii')
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.3/encodings/ascii.py", line 26, in decode
    return codecs.ascii_decode(input, self.errors)[0]
UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position
12: ordinal not in range(128)
>>>

>>> # Replace bad chars with Unicode U+fffd replacement char
>>> f = open('sample.txt', 'rt', encoding='ascii', errors='replace')
>>> f.read()
'Spicy Jalape?o!'
>>> # Ignore bad chars entirely
>>> g = open('sample.txt', 'rt', encoding='ascii', errors='ignore')
>>> g.read()
'Spicy Jalapeo!'
>>>
