prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
prices_sorted = sorted(zip(prices.values(), prices.keys()))

In [24]: min_price = min(zip(prices.values(), prices.keys()))
In [25]: print(min_price)
(10.75, 'FB')

In [26]: max_price = max(zip(prices.values(), prices.keys()))
In [27]: print(max_price)
(612.78, 'AAPL')

In [28]: prices_sorted = sorted(zip(prices.values(), prices.keys()))
In [29]: print(prices_sorted)
[(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL
)]

In [30]: min(prices)
Out[30]: 'AAPL'
In [31]: max(prices)
Out[31]: 'IBM'

In [32]: min(prices.values())
Out[32]: 10.75
In [33]: max(prices.values())
Out[33]: 612.78

In [34]: min(prices, key=lambda k: prices[k])
Out[34]: 'FB'
In [35]: max(prices, key=lambda k: prices[k])
Out[35]: 'AAPL'

In [36]: min_value = prices[min(prices, key=lambda k: prices[k])]
In [37]: print(min_value)
10.75

In [38]: max_value = prices[max(prices, key=lambda k: prices[k])]
In [39]: print(max_value)
612.78
In [40]:
