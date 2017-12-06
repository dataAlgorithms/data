#!/usr/bin/env python3
#coding=utf-8

from multiprocessing import Pool

def test(i):
    print(i)

"""
说明：for循环内执行的步骤顺序，往进程池中添加一个子进程，执行子进程，等待执行完毕再添加一个子进程…..等500个子进程都执行完了，再执行print “test”。（从结果来看，并没有多进程并发）
"""

if __name__ == "__main__":
    pool = Pool(processes=10)
    for i in range(500):
        """
实际测试发现，for循环内部执行步骤：
    （1）遍历500个可迭代对象，往进程池放一个子进程
    （2）执行这个子进程，等子进程执行完毕，再往进程池放一个子进程，再执行。（同时只执行一个子进程）
    for循环执行完毕，再执行print函数。
        """
        pool.apply(test, args=(i, ))

    print("test start")
    pool.close()
    pool.join()
    print("test done")