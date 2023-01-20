## 141
"""
print price with tax.
tax is 10 krw
"""
list = [100, 200, 300]
for price in list:
  print(price + 10)

## 142
"""
print like example.

list = ['apple', 'banana', 'kiwi']
---
menu : apple
menu : banana
menu : kiwi
"""
list = ['apple', 'banana', 'kiwi']
for menu in list:
  print("menu :", menu)

## 143
"""
print length of list elem
"""
list = ['apple', 'banana', 'kiwi']
for menu in list:
  print(len(menu))

## 144
"""
print animal name and length
"""
list = ['dog', 'cat', 'parrot']
for animal in list:
  print(animal, len(animal))

## 145
"""
print first character of list elem
"""
list = ['dog', 'cat', 'parrot']
for animal in list:
  print(animal[0])

## 146
"""
print like example

list = [1, 2, 3]
---
3 x 1
3 x 2
3 x 3
"""
list = [1, 2, 3]
for i in list:
  print("3 x", i)

## 147
"""
print like example

list = [1, 2, 3]
---
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
"""
list = [1, 2, 3]
for i in list:
  print(f"3 x {i} = {3 * i}")

## 148
"""
print like example

list = ['a', 'b', 'c', 'd']
---
b
c
d
"""
list = ['a', 'b', 'c', 'd']
for char in list[1:]:
  print(char)

## 149
"""
print like example

list = ['a', 'b', 'c', 'd']
---
a
c
"""
list = ['a', 'b', 'c', 'd']

"""
<method1>
for i in range(0, 4, 2):
  print(list[i])
"""

for char in list[::2]:
  print(char)

## 149
"""
print like example

list = ['a', 'b', 'c', 'd']
---
d
c
b
a
"""
list = ['a', 'b', 'c', 'd']
for char in list[::-1]:
  print(char)
