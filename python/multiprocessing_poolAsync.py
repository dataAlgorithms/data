#!/usr/bin/env python3
#coding=utf-8

from multiprocessing import Pool

def test(i):
    print(i)

"""
执行顺序：For循环内执行了2个步骤，
第一步：将500个对象放入进程池（阻塞）。
第二步：同时执行10个子进程（非阻塞），有结束的就立即添加，维持10个子进程运行。
（apply_async方法的会在执行完for循环的添加步骤后，直接执行后面的print语句，
 而apply方法会等所有进程池中的子进程运行完以后再执行后面的print语句）

注意：调用join之前，先调用close或者terminate方法，否则会出错。
执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束。
"""

if __name__ == "__main__":
    pool = Pool(processes=10)
    for i in range(500):
        """
        循环遍历. 将500个子进程添加到进程池 (相对父进程会阻塞)
        每次执行10个子进程, 等一个子进程执行完后, 立马启动新的子进程 (相对父进程不阻塞)

        apply_async为异步进程池写法
        异步指的是启动子进程的过程, 与父进程本身的执行(print)是异步的
                for循环中往进程池添加子进程的过程, 与父进程本身的执行是同步的.
        """
        pool.apply_async(test, args=(i, ))

    print("test start")
    pool.close()
    pool.join()
    print("test done")