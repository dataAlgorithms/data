#!/usr/bin/env python
#coding=utf-8

from Queue import Queue
import random
import threading
import time

class Producer(threading.Thread):
    '''
    Producer thread
    '''
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue

    def run(self):
        for i in range(5):   # generate 0~4 queue
            print "%s: %s is producing %d to the queue!" %(time.ctime(), self.getName(), i) # join the queue
            self.data.put(i)   # write queue number
            time.sleep(random.randrange(10) / 5) # wait for a while
        print "%s: %s producing finished!" % (time.ctime(), self.getName)

class Consumer(threading.Thread):
    '''
    Consumer thread
    '''
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue

    def run(self):
        for _ in range(5):
            val = self.data.get()
            print "%s: %s is consumering. %d in the queue is consumed!" % (time.ctime(), self.getName(), val)
            time.sleep(random.randrange(10))
        print "%s: %s consuming finished" % (time.ctime(), self.getName())

'''
Mon Dec 04 16:04:25 2017: Pro. is producing 0 to the queue!
Mon Dec 04 16:04:25 2017: Con. is consumering. 0 in the queue is consumed!
Mon Dec 04 16:04:26 2017: Pro. is producing 1 to the queue!
Mon Dec 04 16:04:27 2017: Pro. is producing 2 to the queue!
Mon Dec 04 16:04:27 2017: Pro. is producing 3 to the queue!
Mon Dec 04 16:04:27 2017: Pro. is producing 4 to the queue!
Mon Dec 04 16:04:28 2017: <bound method Producer.getName of <Producer(Pro., started 10908)>> producing finished!
Mon Dec 04 16:04:29 2017: Con. is consumering. 1 in the queue is consumed!
Mon Dec 04 16:04:35 2017: Con. is consumering. 2 in the queue is consumed!
Mon Dec 04 16:04:43 2017: Con. is consumering. 3 in the queue is consumed!
Mon Dec 04 16:04:51 2017: Con. is consumering. 4 in the queue is consumed!
Mon Dec 04 16:04:53 2017: Con. consuming finished
All threads terminate!
'''
def main():
    queue = Queue()
    producer = Producer('Pro.', queue)
    consumer = Consumer('Con.', queue)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    print "All threads terminate!"

if __name__ == "__main__":
    main()
