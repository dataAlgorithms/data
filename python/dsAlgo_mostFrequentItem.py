In [39]: %paste
words = [
   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
   'my', 'eyes', "you're", 'under'
]

## -- End pasted text --

In [40]: from collections import Counter

In [41]: word_counts = Counter(words)

In [42]: top_three = word_counts.most_common(3)

In [43]: print(top_three)
[('eyes', 8), ('the', 5), ('look', 4)]

In [44]: word_counts['not']
Out[44]: 1

In [45]: word_counts['eyes']
Out[45]: 8

In [46]: morewords = ['why','are','you','not','looking','in','my','eyes']

In [47]: word_counts.update(morewords)

In [48]: word_counts
Out[48]:
Counter({'are': 1,
         'around': 2,
         "don't": 1,
         'eyes': 9,
         'in': 1,
         'into': 3,
         'look': 4,
         'looking': 1,
         'my': 4,
         'not': 2,
         'the': 5,
         'under': 1,
         'why': 1,
         'you': 1,
         "you're": 1})

In [49]: a = Counter(words)

In [50]: b = Counter(morewords)

In [51]: a
Out[51]:
Counter({'around': 2,
         "don't": 1,
         'eyes': 8,
         'into': 3,
         'look': 4,
         'my': 3,
         'not': 1,
         'the': 5,
         'under': 1,
         "you're": 1})

In [52]: b
Out[52]:
Counter({'are': 1,
         'eyes': 1,
         'in': 1,
         'looking': 1,
         'my': 1,
         'not': 1,
         'why': 1,
         'you': 1})

In [53]: c = a + b

In [54]: c
Out[54]:
Counter({'are': 1,
         'around': 2,
         "don't": 1,
         'eyes': 9,
         'in': 1,
         'into': 3,
         'look': 4,
         'looking': 1,
         'my': 4,
         'not': 2,
         'the': 5,
         'under': 1,
         'why': 1,
         'you': 1,
         "you're": 1})

In [55]: d = a - b

In [56]: d
Out[56]:
Counter({'around': 2,
         "don't": 1,
         'eyes': 7,
         'into': 3,
         'look': 4,
         'my': 2,
         'the': 5,
         'under': 1,
         "you're": 1})
