## 111
# print input twice
user = input()
print(user * 2)

## 112
# print input + 10
user = input("integer : ")
print(int(user) + 10) # careful! user is <class 'str'>

## 113
# print oddity of input
user = input("integer : ")

if (int(user) % 2 == 0):
  print("even")
else:
  print("odd")
  
## 114
# print min(255, input + 20)
user = input("integer : ")
result = int(user) + 20

print(min(255, result)) # or implement it using if/else

## 115
# print input - 20 cut to [0, 255] range
user = input("integer : ")
result = int(user) - 20

if result < 0:
  print(0)
elif result > 255:
  print(255)
else:
  print(result)
  
## 116
# determine time is ~~:00
user = input("time : ")
min = int(user.split(':')[1])
if min == 0:
  print("o'clock")
else:
  print("not o'clock")

""" Official Solution
if user[-2:] == "00":
else:
"""

## 117
# print whether input is in list or not
fruit = ['apple', 'grape', 'banana']
user = input("fruit : ")
if user in fruit:
  print("Yes")
else:
  print("No")

## 118
# print whether input is in list or not
warn_invest_list = ["MS", "Google", "Naver", "Kakao", "Samsung"]
user = input('one company : ')
if user in warn_invest_list:
  print("warning!")
else:
  print("safe!")
  
## 119
# print whether input is in dictionary key or not
fruit = {
  'spring' : 'strawberry',
  'summer' : 'tomato',
  'fall' : 'apple'
}

user = input('one input (key): ')
if user in fruit:
  print("Yes")
else:
  print("No")
  
## 120
# print whether input is in dictionary value or not
fruit = {
  'spring' : 'strawberry',
  'summer' : 'tomato',
  'fall' : 'apple'
}

user = input('one input (value): ')
# use values() method to target value
if user in fruit.values():
  print("Yes")
else:
  print("No")
