In [8]: import heapq
In [9]: 
In [9]: nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
In [10]: print(heapq.nlargest(3, nums))
[42, 37, 23]
In [11]: print(heapq.nsmallest(3, nums))
[-4, 1, 2]

In [12]: portfolio = [
    ...:     {'name': 'IBM', 'shares': 100, 'price': 91.1},
    ...:     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    ...:     {'name': 'FB', 'shares': 200, 'price': 21.09},
    ...:     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    ...:     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    ...:     {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ...: ]
In [13]: 
In [13]: cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
In [14]: expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
In [3]: print(cheap)
[{'price': 16.35, 'name': 'YHOO', 'shares': 45}, {'price': 21.09, 'name': 'FB',
'shares': 200}, {'price': 31.75, 'name': 'HPQ', 'shares': 35}]
In [4]: print(expensive)
[{'price': 543.22, 'name': 'AAPL', 'shares': 50}, {'price': 115.65, 'name': 'ACM
E', 'shares': 75}, {'price': 91.1, 'name': 'IBM', 'shares': 100}]

In [15]: nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
In [5]: nums
Out[5]: [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
In [6]: import heapq
In [7]: type(nums)
Out[7]: list
In [8]: heap = nums
In [9]: heapq.heapify(heap)
In [10]: heap
Out[10]: [-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]
In [11]: heapq.heappop(heap)
Out[11]: -4
In [12]: heapq.heappop(heap)
Out[12]: 1
In [13]: heapq.heappop(heap)
Out[13]: 2
