from functools import partial

def spam(a, b, c, d):
    print(a, b, c, d)

s1 = partial(spam, 1)
s1(2, 3, 4)
s1(4, 5, 6)
s2 = partial(spam, d=42)
s2(1, 2, 3)
s2(4, 5, 5)
s3 = partial(spam, 1, 2, d=42)
s3(3)
s3(4)
s3(5)

'''
1 2 3 4
1 4 5 6
1 2 3 42
4 5 5 42
1 2 3 42
1 2 4 42
1 2 5 42
'''

import math

points = [(1, 2), (3, 4), (5, 6), (7, 8)]
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)

pt = (4, 3)
points.sort(key=partial(distance, pt))
print(points)

'''
[(3, 4), (1, 2), (5, 6), (7, 8)]
'''

def output_result(result, log=None):
    if log is None:
        log.debug('Got: %r', result)

# A sample function
def add(x, y):
    return x + y
    print(x + y)

if True:
    import logging
    from multiprocessing import Pool
    from functools import partial

    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('test')

    p = Pool()
    p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
    p.close()
    p.join()
    
class EchoHandler(StreamRequestHandler):
    # ack is added keyword-only argument, *args, **kwargs are
    # any normal parameters supplied (which are passed on)
    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        super().__init__(*args, **kwargs)
    def handle(self):
        for line in self.rfile:
            self.wfile.write(self.ack + line)

from functools import partial
serv = TCPServer(('', 15000), partial(EchoHandler, ack=b'RECEIVED:'))
serv.serve_forever()
