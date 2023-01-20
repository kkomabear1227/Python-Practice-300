## 201
"""
define function print_coin() which prints 'btc'
"""
def print_coin():
  print('btc')

## 202
"""
call print_coin()
"""
print_coin()

## 203
"""
call print_coin() 100 times
"""
for i in range(100):
  print_coin()

## 204
"""
define function print_coins() which clal print_coin() 100 times
"""
def print_coins():
  for i in range(100):
    print_coins() # or simply print('btc')
    
## 205
"""
describe why this code errors.

hello()
def hello():
    print("Hi")
"""
# function called before declaration

## 206
"""
predict the result

def message() :
    print("A")
    print("B")

message()
print("C")
message()
"""
# A\nB\nC\nA\nB\n

## 207
"""
predict the result.
(this code is example of bad readability)

print("A")

def message() :
    print("B")

print("C")
message()
"""
#A\nC\nB\n

## 208
"""
predict the result.
(this code is example of bad readability)

print("A")
def message1() :
    print("B")
print("C")
def message2() :
    print("D")
message1()
print("E")
message2()
"""
#A\nC\nB\nD\n

## 209
"""
predict the result

def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()
"""
#B\nA\n

## 210
"""
predict the result

def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()
"""
#B\nC\bB\nC\nB\nC\nA\n
