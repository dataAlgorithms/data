prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

# Make a dictionary of all prices over 200
priceAbove200 = {key:value for key, value in prices.items() if value > 200}
print(priceAbove200)

//output
{'AAPL': 612.78, 'IBM': 205.55}

priceAbove200Slow = dict((key, value) for key, value in prices.items() if value > 200)
print(priceAbove200Slow)

//output
{'AAPL': 612.78, 'IBM': 205.55}

# Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', "HPQ", 'MSFT'}
stockIn = {key:value for key, value in prices.items() if key in tech_names}
print(stockIn)

//output
{'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.2}

stockInSlow = {key:prices[key] for key in prices.keys() & tech_names}
print(stockInSlow)

//output
{'AAPL': 612.78, 'HPQ': 37.2, 'IBM': 205.55}
