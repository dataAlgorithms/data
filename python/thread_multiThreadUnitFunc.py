#!/usr/bin/env python
#coding=utf-8

from time import sleep, ctime
import threading

def super_player(filename, time):
    for _ in range(2):
        print 'Start playing: %s! %s' % (filename, ctime())
        sleep(time)

lst = {'love.mp3': 3, 'afanda.mp4': 5, 'youandme.mp3': 4}

threads = []
files = range(len(lst))

for filename, time in lst.items():
    t = threading.Thread(target=super_player, args=(filename,time))
    threads.append(t)

'''
Start playing: afanda.mp4! Mon Dec 04 15:10:26 2017
Start playing: love.mp3! Mon Dec 04 15:10:26 2017
Start playing: youandme.mp3! Mon Dec 04 15:10:26 2017
Start playing: love.mp3! Mon Dec 04 15:10:29 2017
Start playing: youandme.mp3! Mon Dec 04 15:10:30 2017
Start playing: afanda.mp4! Mon Dec 04 15:10:31 2017
end: Mon Dec 04 15:10:36 2017
'''
if __name__ == "__main__":
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()

    print 'end: %s' % ctime()
