s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)

//output
pýtĥöñis       awesome



remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\t'): None
}

a = s.translate(remap)
print(a)

//output
pýtĥöñ isawesome

import unicodedata
import sys

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
              if unicodedata.combining(chr(c)))

b = unicodedata.normalize('NFD', a)
print(b)
print(b.translate(cmb_chrs))

//output
pýtĥöñ isawesome

python isawesome

digitmap = {c: ord('0') + unicodedata.digit(chr(c))
             for c in range(sys.maxunicode)
             if unicodedata.category(chr(c)) == 'Nd'}

x = '\u0661\u0662\u0663'
print(x.translate(digitmap))

//output
123

print(a)
b = unicodedata.normalize('NFD', a)
print(b.encode('ascii', 'ignore').decode('ascii'))

//output
pýtĥöñ isawesome

python isawesome

def clean_spaces(s):
    s = s.replace('\r', '')
    s = s.replace('\t', ' ')
    s = s.replace('\f', ' ')
    return s
