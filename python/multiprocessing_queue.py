#!/usr/bin/env python3 
#coding=utf-8

from multiprocessing import Process, Queue

def consumer(imput_q):
    while True:
        item = imput_q.get()
        if item is None:
            break

        print(item)

    print("Consumer done!")

def producer(sequence, output_q):
    for item in sequence:
        output_q.put(item)

'''
1
2
3
4
Consumer done!
'''
if __name__ == "__main__":
    
    q = Queue()

    #启动使用者进程
    cons_p = Process(target=consumer, args=(q,))
    cons_p.start()

    #生产项目
    sequence = [1, 2, 3, 4]
    producer(sequence, q)

    #在队列上安置标志 发出完成信号
    q.put(None)

    #等待使用者进程关闭
    cons_p.join()