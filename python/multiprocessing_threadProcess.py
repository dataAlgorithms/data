#!/usr/bin/env python3
#coding=utf-8 

from multiprocessing import Pool
from queue import Queue
import threading
import time

def test(p):
    time.sleep(0.001)
    if p == 10000:
        return True
    else:
        return False

if __name__ == "__main__":

    result = Queue()
    pool = Pool()

    def pool_th():
        for  i in range(5000000):
            try:
                result.put(pool.apply_async(test, args=(i, )))
            except:
                break

    def result_th():
        while True:
            a = result.get().get() #获取子进程返回值
            if a:
                pool.terminate() #结束所有子进程
                break

    '''
              利用多线程，同时运行Pool函数创建执行子进程，以及运行获取子进程返回值函数。
    '''
    t1 = threading.Thread(target=pool_th)
    t2 = threading.Thread(target=result_th)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    pool.join()