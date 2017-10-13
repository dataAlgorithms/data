In [1]: !more somefile
无法访问 D:\Program Files\Anaconda3\Scripts\somefile 文件

In [2]: with open('somefile', 'wt') as f:
   ...:     f.write('Hello\n')
   ...:

In [3]: with open('somefile', 'xt') as f:
   ...:     f.write('Hello\n')
   ...:
---------------------------------------------------------------------------
FileExistsError                           Traceback (most recent call last)
<ipython-input-3-649cb3f23751> in <module>()
----> 1 with open('somefile', 'xt') as f:
      2     f.write('Hello\n')
      3

FileExistsError: [Errno 17] File exists: 'somefile'

In [4]: import os

In [6]: if not os.path.exists('somefile'):
   ...:     with open('somefile', 'wt') as f:
   ...:         f.write('Hello\n')
   ...: else:
   ...:     print('File already exists!')
   ...:
File already exists!

小结:
1. 如果只写内容到 不存在的文件中
文本文件: 使用xt
二进制文件: 使用xb

2. 替代方式
可以先通过os.exists判断文件是否存在, 如果不存在才写, 否则不写文件
