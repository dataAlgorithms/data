#!/usr/bin/env python3
#coding=utf-8

from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self, arg):
        super(MyProcess, self).__init__()
        self.arg = arg
    def run(self):
        print('nMask', self.arg)
        time.sleep(1)

"""
nMask 4
nMask 2
nMask 5
nMask 7
nMask 3
nMask 6
nMask 9
nMask 8
nMask 1
nMask 0
"""
if __name__ == "__main__":
    for i in range(10):
        p = MyProcess(i)
        p.start()
    for i in range(10):
        p.join() 