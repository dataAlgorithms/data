#!/usr/bin/env python
#coding=utf-8

# 多线程

import threading
from time import ctime, sleep

def music(func):
    for _ in range(2):
        print "I was listening to %s. %s" % (func, ctime())
        sleep(1)

def movie(func):
    for _ in range(2):
        print "I was at the %s! %s" % (func, ctime())
        sleep(5)

threads = []
t1 = threading.Thread(target=music, args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=movie, args=(u'阿凡达',))
threads.append(t2)

'''
I was listening to 爱情买卖. Mon Dec 04 14:13:52 2017
 I was at the 阿凡达! Mon Dec 04 14:13:52 2017
I was listening to 爱情买卖. Mon Dec 04 14:13:53 2017
I was at the 阿凡达! Mon Dec 04 14:13:57 2017

all over Mon Dec 04 14:14:02 2017
'''
if __name__ == "__main__":
    for t in threads:
        t.setDaemon(True)  #将线程声明为守护线程，必须在start() 方法调用之前设置
        t.start()

    t.join()   #在子线程完成运行之前，这个子线程的父线程将一直被阻塞
    
    print "\rall over %s" % ctime()
