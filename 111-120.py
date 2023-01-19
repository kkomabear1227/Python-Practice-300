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

