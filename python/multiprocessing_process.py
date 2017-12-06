#!/usr/bin/env python3
#coding=utf-8 

from multiprocessing import Process
import os

def test(name):
    print("Process ID: %s" % (os.getpid()))
    print("Parent Process ID: %s" % (os.getppid()))

'''
Process ID: 10036
Parent Process ID: 6532
'''
if __name__ == "__main__":
    proc = Process(target=test, args=('nmask',))
    proc.start()
    proc.join()