text = 'UPPER PYTHON, lower python, Mixed Python'
re.findall('python', text, flags=re.IGNORECASE)
re.sub('python', 'snake', text, flags=re.IGNORECASE)

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)

//output
In [75]: text = 'UPPER PYTHON, lower python, Mixed Python'

In [76]: re.findall('python', text, flags=re.IGNORECASE)
Out[76]: ['PYTHON', 'python', 'Python']

In [78]: re.sub('python', 'snake', text, flags=re.IGNORECASE)
Out[78]: 'UPPER snake, lower snake, Mixed snake'

In [79]: %paste
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)

## -- End pasted text --
Out[79]: 'UPPER SNAKE, lower snake, Mixed Snake'

