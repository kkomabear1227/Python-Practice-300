## 211
"""
predict the result.

def func(str):
  print(str)

func("Hello")
func("World")
"""
# Hello\nWorld\n

## 212
"""
predict the result.
def func(a, b) :
    print(a + b)

func(3, 4)
func(7, 8)
"""
# 7\n15\n

## 213
"""
describe why error occurs

def func(str):
  print(str)

func()
"""
#function call doesn't match with function declaration

## 214
"""
describe why error occurs

def func(a, b) :
    print(a + b)

func("Hello", 3)
"""
#using function with unintended way.

## 215
"""
define a function which print argument string and ':D'
"""
def print_with_smile(str):
  print(str + ' :D')

## 216
"""
call function print_with_smile()
"""
print_with_smile("Hello")

## 217
"""
define function print_upper_price() which prints 30% upper price of the argument 'price'
"""
def print_upper_price(price):
  print(price * 1.3)
print_upper_price(10000)

## 218
"""
define function print_sum() which prints sum of the argument 'a', 'b'
"""
def print_sum(a, b):
  print(a + b)
print_sum(1, 2)

## 219
"""
define function which prints four arithmetic operation results of argument 'a', 'b'

function name should be 'print_arithmetic_operation'
"""
def print_arithmetic_operation(a, b):
  print(a + b)
  print(a - b)
  print(a * b)
  print(a / b)
print_arithmetic_operation(3, 2)

## 220
"""
define function print_max() which get 3 argument 'a', 'b', 'c' and prints maximum value.

should not use max(). if-statement is only allowed
"""
def print_max(a, b, c):
  if a >= b and a >= c:
    print(a)
  elif b >= a and b >= c:
    print(b)
  else:
    print(c)
