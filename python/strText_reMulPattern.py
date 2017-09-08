import re

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/*this is a comment*/'
text2 = '''/*this is a 
              multiline comment*/'''

comment.findall(text1)
comment.findall(text2)

comment = re.compile(r'/\*((?:.|\n)*?)\*/')
comment.findall(text2)

comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
comment.findall(text2)

//output
In [83]: import re
    ...:
    ...: comment = re.compile(r'/\*(.*?)\*/')
    ...: text1 = '/*this is a comment*/'
    ...: text2 = '''/*this is a
    ...:               multiline comment*/
    ...:
    ...:
    ...: '''
    ...:

In [84]: comment.findall(text1)
Out[84]: ['this is a comment']

In [85]: comment.findall(text2)
Out[85]: []

In [86]: comment = re.compile(r'/\*((?:.|\n)*?)\*/')
    ...: comment.findall(text2)
    ...:
Out[86]: ['this is a \n              multiline comment']

In [87]:
    ...: comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
    ...: comment.findall(text2)
    ...:
Out[87]: ['this is a \n              multiline comment']
