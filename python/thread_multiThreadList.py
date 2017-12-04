#!/usr/bin/env python
#coding=utf-8

from time import sleep, ctime
import threading

def music(func):
    for _ in range(2):
        print 'Start playing: %s! %s' % (func, ctime())
        sleep(2)

def movie(func):
    for _ in range(2):
        print 'Start playing: %s! %s' % (func, ctime())
        sleep(5)

def player(name):
    r = name.split('.')[1]
    if r == 'mp3':
        music(name)
    else:
        if r == 'mp4':
            movie(name)
        else:
            print 'error: the format is not recognized!'

lst = [u'爱情公寓.mp3', u'阿凡达.mp4']

threads = []
files = range(len(lst))

for i in files:
    t = threading.Thread(target=player, args=(lst[i],))
    threads.append(t)

'''
Start playing: 爱情公寓.mp3! Mon Dec 04 15:01:19 2017
Start playing: 阿凡达.mp4! Mon Dec 04 15:01:19 2017
Start playing: 爱情公寓.mp3! Mon Dec 04 15:01:21 2017
Start playing: 阿凡达.mp4! Mon Dec 04 15:01:24 2017
end:Mon Dec 04 15:01:29 2017
'''
if __name__ == "__main__":
    for i in files:
        threads[i].start()

    for i in files:
        threads[i].join()

    print 'end:%s' % ctime()
