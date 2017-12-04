#!/usr/bin/env python
#coding=utf-8

# 单现程
print ":::单线程!"

from time import ctime, sleep

def music(func):
    for _ in range(2):
        print "I was listening to %s. %s" % (func, ctime())
        sleep(1)

def movie(func):
    for _ in range(2):
        print "I was at the %s! %s" % (func, ctime())
        sleep(5)

'''
:::单线程!
I was listening to 爱情买卖. Mon Dec 04 14:00:38 2017
I was listening to 爱情买卖. Mon Dec 04 14:00:39 2017
I was at the 阿凡达! Mon Dec 04 14:00:40 2017
I was at the 阿凡达! Mon Dec 04 14:00:45 2017
all over Mon Dec 04 14:00:50 2017
'''
if __name__ == "__main__":
    music(u'爱情买卖')
    movie(u'阿凡达')
    print "all over %s" % ctime()
