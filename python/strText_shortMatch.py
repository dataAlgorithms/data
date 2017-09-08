import re
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
str_pat.findall(text1)

//output
Out[80]: ['no.']

text2 = 'Computer says "no." Phone says "yes."'
str_pat.findall(text2)

//output
Out[81]: ['no." Phone says "yes.']

str_pat = re.compile(r'\"(.*?)\"')
str_pat.findall(text2)

//output
Out[82]: ['no.', 'yes.']
