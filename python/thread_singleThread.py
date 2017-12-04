#!/usr/bin/env python
#coding=utf-8

# 单线程
print ":::单线程!"

from time import ctime, sleep

def music():
    for _ in range(2):
        print "I was listening to music. %s" % ctime()
        sleep(1)

def movie():
    for _ in range(2):
        print "I was at the movies! %s" % ctime()
        sleep(5)

'''
:::单线程!
I was listening to music. Mon Dec 04 13:51:16 2017
I was listening to music. Mon Dec 04 13:51:17 2017
I was at the movies! Mon Dec 04 13:51:18 2017
I was at the movies! Mon Dec 04 13:51:23 2017
all over Mon Dec 04 13:51:28 2017
'''
if __name__ == "__main__":
    music()
    movie()
    print "all over %s" % ctime()
