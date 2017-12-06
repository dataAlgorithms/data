#!/usr/bin/env python3
#coding=utf-8 

from multiprocessing import Process, Array

def test(a):
    for i in range(len(a)):
        a[i] = -a[i]

'''
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
'''
if __name__ == "__main__":
    arr = Array('i', range(10))
    p = Process(target=test, args=(arr,))
    p.start()
    p.join()
    print(arr[:])