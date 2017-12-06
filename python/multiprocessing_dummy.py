#!/usr/bin/env python3
#coding=utf-8

from multiprocessing.dummy import Pool as ThreadPool
import time
import requests

urls = [  
    'http://www.python.org',   
    'http://www.python.org/about/',  
    'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',  
    'http://www.python.org/doc/',  
    'http://www.python.org/download/',  
    'http://www.python.org/getit/',  
    'http://www.python.org/community/',  
    'https://wiki.python.org/moin/',  
    'http://planet.python.org/',  
    'https://wiki.python.org/moin/LocalUserGroups',  
    'http://www.python.org/psf/',  
    'http://docs.python.org/devguide/',  
    'http://www.python.org/community/awards/'  
    ]  

# 单线程
start = time.time()
for url in urls:
    results  = requests.get(url)
print('Normal: ', time.time() - start)

# 多线程
start2 = time.time()
# 开4个worker, 没有参数默认是cpu的核心数
pool = ThreadPool(4)
results2 = pool.map(requests.get, urls)
pool.close()
pool.join()
print('Thread pool:', time.time() -start2)

'''
Normal:  31.48780083656311
Thread pool: 8.31747579574585
'''