import re

num = re.compile('\d+')
print(num.match('123'))
print(num.match('\u0661\u0662\u0663'))

//output
<_sre.SRE_Match object; span=(0, 3), match='123'>
<_sre.SRE_Match object; span=(0, 3), match='١٢٣'>

arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')

//output
Out[12]: re.compile(r'[\u0600-ۿݐ-ݿࢠ-ࣿ]+', re.UNICODE)

pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
print(pat.match(s))
print(s.upper())

//output
<_sre.SRE_Match object; span=(0, 6), match='straße'>
STRASSE
