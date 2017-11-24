import time
from threading import Thread 

#################common task
class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(5)

c = CountdownTask()
t = Thread(target=c.run, args=(10,))
t.start()
time.sleep(10)
c.terminate()
t.join()

'''
('T-minus', 10)
('T-minus', 9)
('T-minus', 8)
'''

###########io
import socket

class IOTask:
    def terminate(self):
        self._running = False

    def run(self, sock):
        # sock is a socket
        sock.settimeout(5)          # Set timeout period
        while self._running:
            # Perform a blocking IO operation w timeout
            try:
                _data = sock.recv(8192)
                break
            except socket.timeout:
                continue
            # Continued processing
        # Terminated
        return
