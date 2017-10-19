In [1]: import os

In [2]: os.path.exists('/etc/passwd')
Out[2]: False

In [3]: os.path.exists('somefile')
Out[3]: True

In [4]: os.path.isfile('somefile')
Out[4]: True

In [5]: os.path.isdir('somefile')
Out[5]: False

In [6]: os.path.realpath('somefile')
Out[6]: 'D:\\Program Files\\Anaconda3\\Scripts\\somefile'

In [7]: os.path.getsize('somefile')
Out[7]: 7

In [8]: os.path.getmtime('somefile')
Out[8]: 1507859411.611115

In [9]: import time

In [10]: time.ctime(os.path.getmtime('somefile'))
Out[10]: 'Fri Oct 13 09:50:11 2017'

In [11]: os.access('somefile', os.R_OK)
Out[11]: True

In [12]: os.access('somefile', os.X_OK)
Out[12]: True

In [13]: os.access('somefile', os.W_OK)
Out[13]: True
