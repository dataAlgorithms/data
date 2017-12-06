#!/usr/bin/env python3
#coding=utf-8

from multiprocessing import Pool

def test(i):
    print(i)

'''
1
2
3
'''
if __name__ == "__main__":
    lists = [1, 2, 3]
    pool = Pool(processes=2) # 最大的进程数
    pool.map(test, lists)
    pool.close()
    pool.join()