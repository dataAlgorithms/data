#!/usr/bin/env python
#coding=utf-8

# test thread join
import threading, time

def doWaiting():
    print 'start waiting1: ' + time.strftime('%H:%M:%S') + "\n"
    time.sleep(3)
    print 'stop waiting1: ' + time.strftime('%H:%M:%S') + "\n"
    
def doWaiting1():
    print 'start waiting2: ' + time.strftime('%H:%M:%S') + "\n"
    time.sleep(8)
    print 'stop waiting2: ', time.strftime('%H:%M:%S') + "\n"

print 'Case1: join without parameter!'
tsk = []
thread1 = threading.Thread(target = doWaiting)
thread1.start()
tsk.append(thread1)
thread2 = threading.Thread(target = doWaiting1)
thread2.start()
tsk.append(thread2)
print 'start join: ' + time.strftime('%H:%M:%S') + "\n"
for tt in tsk:
    tt.join()
print 'end join: ' + time.strftime('%H:%M:%S') + "\n"

'''
输出：
start waiting1: 08:39:04
start waiting2: 08:39:04
start join: 08:39:04
stop waiting1: 08:39:07
stop waiting2:  08:39:12
end join: 08:39:12

结果分析：
1. 两个线程在同一时间开启，join 函数执行。
2. waiting1 线程执行（等待）了3s 以后，结束。
3. waiting2 线程执行（等待）了8s 以后，运行结束。
4. join 函数（返回到了主进程）执行结束。
'''

print ""

print 'Case2: Join with timeout parameter'
tsk = []
thread1 = threading.Thread(target = doWaiting)
thread1.start()
tsk.append(thread1)
thread2 = threading.Thread(target = doWaiting1)
thread2.start()
tsk.append(thread2)
print 'start join: ' + time.strftime('%H:%M:%S') + "\n"
for tt in tsk:
    tt.join(2)
print 'end join: ' + time.strftime('%H:%M:%S') + "\n"

'''
Case2: Join with timeout parameter
start waiting1: 09:18:45
start waiting2: 09:18:45
start join: 09:18:45
stop waiting1: 09:18:48
end join: 09:18:49
stop waiting2:  09:18:53

分析：
1. 两个线程在同一时间开启，join 函数执行。
2. wating1 线程在执行（等待）了三秒以后，完成。
3. join 退出（两个2s，一共4s，36-32=4，无误）。
4. waiting2 线程由于没有在 join 规定的等待时间内（4s）完成，所以自己在后面执行完成。
'''
