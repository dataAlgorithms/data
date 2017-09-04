import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
q.pop()
q.pop()
q.pop()
q.pop()



In [18]: q = PriorityQueue()
In [19]: q.push(Item('foo'), 1)
In [20]: q.push(Item('bar'), 5)
In [21]: q.push(Item('spam'), 4)
In [22]: q.push(Item('grok'), 1)
In [23]: q.pop()
Out[23]: Item('bar')
In [24]: q.pop()
Out[24]: Item('spam')
In [25]: q.pop()
Out[25]: Item('foo')
In [26]: q.pop()
Out[26]: Item('grok')
