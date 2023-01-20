## 221
"""
define function print_reverse() which prints argument string 'str' in reverse.
"""
def print_reverse(str):
  print(str[::-1])
print_reverse('hello')

## 222
"""
define function print_score() which gets list and prints average of list elem.
"""
def print_score(list):
  print(sum(list) / len(list))

print_score([1, 2, 3])

## 223
"""
define function print_even which prints even number in the list
"""
def print_even(list):
  for elem in list:
    if elem % 2 == 0:
      print(elem)

print_even ([1, 3, 2, 10, 12, 11, 15])

## 224
"""
define function print_keys which gets dictionary and prints key of the dictionary.
"""
def print_keys(dict):
  for elem in dict.keys():
    print(elem)
print_keys({'name':'ohm', 'age':23})

## 225
"""
define function print_value_by_key function which gets dictionary name and key, prints value.
"""
def print_value_by_key(dict, key):
  print(dict[key])

my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
print_value_by_key  (my_dict, "10/26")

## 226 (*)
"""
define function print_5xn(str) which prints input string 5 character in oneline.
"""
def print_5xn(str):
  block = int(len(str) / 5)
  for i in range(block + 1):
    print(str[5*i : 5*i + 5])
print_5xn("abcdefghijk")

## 227 
"""
define function print_mxn(str, m) which prints input string m character in oneline
"""
def print_mxn(str, m):
  block = int(len(str) / m)
  for i in range(block + 1):
    print(str[m*i : m*i + m])
print_mxn("asldkfjal", 2)

## 228
"""
define function which calculates monthly_salary from annual_salary.
discard floating point
"""
def calc_monthly_salary(annual_salary):
  print(int(annual_salary / 12))
calc_monthly_salary(11000000)

## 229
"""
predict the result.

def my_print (a, b) :
    print("left:", a)
    print("right:", b)

my_print(a=100, b=200)
"""
# left: 100
# right: 200

## 230
"""
predict the result.

def my_print (a, b) :
    print("left:", a)
    print("right:", b)

my_print(b=100, a=200)
"""
# explcit variable bounding! (not by location)
# left: 200
# right: 100
