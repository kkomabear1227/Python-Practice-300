## 231
"""
predict the result.

def n_plus_1 (n) :
    result = n + 1

n_plus_1(3)
print (result)
"""
# error : cannot access variable inside function. 
# (local scope?)

## 232
"""
define function make_url(site) which returns internet address

make_url("google")
>> https://google.com
"""
def make_url(site):
  print("https://{}.com".format(site))
make_url("google")

## 233
"""
define function make_list(str) which returns list of str character
"""
def make_list(str):
  # list comprehension
  return [char for char in str]
print(make_list("abc"))

## 234
"""
define function pickup_even(list) which returns extracted even number list from argument list.
"""
def pickup_even(list):
  return [num for num in list if num%2 == 0]
print(pickup_even([3, 4, 5, 6, 7, 8]))


## 235
"""
define function convert_int(str) which gets number string (including comma) and returns number
"""
def convert_int(str):
  return int(str.replace(',',''))
print(convert_int("1,234,567"))

## 236
"""
predict the result

def func(num) :
    return num + 4

a = func(10)
b = func(a)
c = func(b)
print(c)
"""
#22

## 237
"""
predict the result

def func(num) :
    return num + 4

c = func(func(func(10)))
print(c)
"""
#22

## 238
"""
def func1(num) :
    return num + 4

def func2(num) :
    return num * 10

a = func1(10)
c = func2(a)
print(c)
"""
#140

## 239
"""
def func1(num) :
    return num + 4

def func2(num) :
    num = num + 2
    return func1(num)

c = func2(10)
print(c)
"""
#16

## 240
"""
def func0(num) :
    return num * 2

def func1(num) :
    return func0(num + 2)

def func2(num) :
    num = num + 10
    return func1(num)

c = func2(2)
print(c)
"""
#28
