#! /usr/bin/env python3
#! coding=utf-8

import threading
import time
import logging
logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s',)  

def connectRedisCheck():
    
    return 1

def checkRedis():
    redisIsOk = 0
    while True:
        time.sleep(3)
        redisIsOk = connectRedisCheck()
        if redisIsOk == 1:
            break

def worker(event):
    logging.debug('Waiting for redis ready...')
    event.wait()
    logging.debug('redis is ready, and connect to redis at [%s]', time.ctime())
    time.sleep(1)
    
redis_ready = threading.Event()
t1 = threading.Thread(target=worker, args=(redis_ready, ), name='t1')
t1.start()

t2 = threading.Thread(target=worker, args=(redis_ready,),name='t2')
t2.start()

logging.debug('check redis server and trigger the redis ready event')
checkRedis()  # simulate the check process
redis_ready.set()

'''
(t1        ) Waiting for redis ready...
(t2        ) Waiting for redis ready...
(MainThread) check redis server and trigger the redis ready event
(t1        ) redis is ready, and connect to redis at [Thu Mar  8 14:54:28 2018]
(t2        ) redis is ready, and connect to redis at [Thu Mar  8 14:54:28 2018]
'''
