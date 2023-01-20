## 091
"""
create dictionary containing below information
dictionary name is 'inventory'

name   | price | #
apple  | 1200  | 20
banana | 1500  | 3
kiwi   | 1000  | 100
"""
inventory = {
  'apple' : [1200, 20],
  'banana' : [1500, 3],
  'kiwi' : [1000, 100]
}

## 092
"""
print price of apple
"""
print(inventory['apple'][0], 'krw')

## 093
"""
print number of apple
"""
print(inventory['apple'][1])

## 094
"""
add new (key, value) in dictionary

watermelon | 2000 | 2
"""
inventory['watermelon'] = [2000, 2]
print(inventory)

## 095
"""
create key list from dictionary 'inventory'
"""
key_list = list(inventory.keys())
print(key_list)

## 096
"""
create value list from dictionary 'inventory'
"""
value_list = list(inventory.values())
print(value_list)

## 097
"""
print sum of price in the following dictionary

fruit = {
  'apple' : 1200,
  'banana' : 1200,
  'watermelon' : 1800,
  'mandarin' : 1800,
  'kiwi' : 1000
}
"""
fruits = {
  'apple' : 1200,
  'banana' : 1200,
  'watermelon' : 1800,
  'mandarin' : 1500,
  'kiwi' : 1000
}
print(sum(fruits.values()))

## 098
"""
add 'new_product' dictionary to 'fruits' dictionary
"""
new_product = {
  'orange' : 1100,
  'mango' : 2100
}
fruits.update(new_product)
print(fruits)

## 099
"""
convert two tuples into dictionary

keys = ("apple", "pear", "peach")
vals = (300, 250, 400)

print(result)
{'apple': 300, 'pear': 250, 'peach': 400}
"""
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)

result = dict(zip(keys, vals))
print(result)

## 100
"""
convert two list into dictionary

date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

print(close_table)
{'09/05': 10500, '09/06': 10300, '09/07': 10100, '09/08': 10800, '09/09': 11000}
"""
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

close_table = dict(zip(date, close_price))
print(close_table)
