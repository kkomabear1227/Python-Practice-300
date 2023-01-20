## 171
"""
print like example using for and range

price_list = [32100, 32150, 32000, 32500]
---
32100
32150
32000
32500
"""
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
  print(price_list[i])

## 172
"""
print like example using for and range

price_list = [32100, 32150, 32000, 32500]
---
0 32100
1 32150
2 32000
3 32500
"""
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
  print(i, price_list[i])

  """
  or we can also use
  for i, data in enumerate(price_list):
    print(i, data)
  """

## 173
"""
print like example using for and range

price_list = [32100, 32150, 32000, 32500]
---
3 32100
2 32150
1 32000
0 32500
"""
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
  print(len(price_list) - 1 - i, price_list[i])

## 174
"""
print like example using for and range

price_list = [32100, 32150, 32000, 32500]
---
100 32150
110 32000
120 32500
"""
price_list = [32100, 32150, 32000, 32500]
for i in range(1,len(price_list)):
  print(90 + 10 * i, price_list[i])

## 175
"""
print like example

my_list = ['a', 'b', 'c', 'd']
---
a b
b c 
c d
"""
my_list = ['a', 'b', 'c', 'd']
for i in range(len(my_list) - 1):
  print(my_list[i], my_list[i+1])

## 176
"""
print like example

my_list = ['a', 'b', 'c', 'd', 'e']
---
a b c
b c d
c d e
"""
my_list = ['a', 'b', 'c', 'd', 'e']
for i in range(len(my_list) - 2):
  print(my_list[i], my_list[i+1], my_list[i+2])

## 175
"""
print like example using for and range

my_list = ['a', 'b', 'c', 'd']
---
d c 
c b
b a
"""
my_list = ['a', 'b', 'c', 'd']
for i in range(len(my_list) - 1):
  print(my_list[len(my_list) - 1 - i], my_list[len(my_list) - 2 - i])

## 178
"""
for each list elem, print diff value with the right side value

my_list = [100, 200, 400, 800]
---
100
200
400
"""
my_list = [100, 200, 400, 800]
for i in range(len(my_list) - 1):
  print(my_list[i+1] - my_list[i])

## 179
"""
print 3-day moving average of the list

my_list = [100, 200, 400, 800, 1000, 1300]
---
233.3333..
466.6666..
733.3333..
1033.3333..
"""
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(len(my_list) - 2):
  sum = my_list[i] + my_list[i+1] + my_list[i+2]
  print(sum / 3)

## 180
"""
using 5-day low_price and high_price, fill 'volatility' list with delta (high_price - low_price)
"""
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = []
for i in range(len(low_prices)):
  volatility.append(high_prices[i] - low_prices[i])

print(volatility)

# list comprehension
volatility2 = [high_prices[i] - low_prices[i] for i in range(len(low_prices))]
print(volatility2)
