>>> import os
>>> import sys
>>> sys.getfilesystemencoding()
'utf-8'
>>> # Write a file using a unicode filename
... 
>>> with open('jalape\xf1o.txt', 'w') as f:
...     f.write('Spicy!')
... 
6
>>> # Directory listing(decoded)
... 
>>> os.listdir('.')
['scgi_params', 'mime.types', 'huoshan.conf', 'uwsgi_params', 'jalape帽o.txt', 'redis.conf', 'fastcgi.conf', 
'killnginx.sh', 'runnginx.sh', 'reload.sh']
>>> 
>>> # Directory listing(raw)
... 
>>> os.listdir(b'.')
[b'scgi_params', b'mime.types', b'huoshan.conf', b'uwsgi_params', b'jalape\xc3\xb1o.txt', b'redis.conf',
b'fastcgi.conf', b'killnginx.sh', b'runnginx.sh', b'reload.sh']
>>> # open file with raw filename
... 

>>> with open(b'jalape\xc3\xb1o.txt') as f:
...     print(f.read())
... 
Spicy!
>>> 



