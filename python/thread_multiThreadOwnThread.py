#!/usr/bin/env python
#coding=utf-8

import threading
from time import sleep, ctime

class MyThread(threading.Thread):

    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
 
    def run(self):
        apply(self.func, self.args)

def super_play(filename, time):
    for _ in range(2):
        print 'Start playing: %s! %s' % (filename, ctime())
        sleep(time)

lst = {'love.mp3':3, 'afd.mp4':5}

threads = []
files = range(len(lst))

for k, v in lst.items():
    t = MyThread(super_play, (k, v), super_play.__name__)
    threads.append(t)

'''
Start playing: afd.mp4! Mon Dec 04 15:17:34 2017
Start playing: love.mp3! Mon Dec 04 15:17:34 2017
Start playing: love.mp3! Mon Dec 04 15:17:37 2017
Start playing: afd.mp4! Mon Dec 04 15:17:39 2017
end: Mon Dec 04 15:17:44 2017
'''
if __name__ == "__main__":
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()

    print 'end: %s' % ctime()
