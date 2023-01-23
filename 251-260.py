## 251
"""
describe class, object, instance
---
ans 
instance of class is object.
"""

## 252
"""
define empty class human.
"""
class Human:
  pass

## 253
"""
create instance of class 'Human'
"""
hyeongmin = Human()

## 254
"""
add constructor which prints "Hi"
"""
class Human:
  def __init__(self):
    print("Hi")

hyeongmin = Human()

## 255
"""
add constructor which gets argument (name, age, gender)
"""
class Human:
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

hyeongmin = Human("Hyeongmin", 23, "male")

## 256
"""
print name, age, gender of the instance created in #255
"""
print("name : {}, age = {}, gender = {}".format(hyeongmin.name, hyeongmin.age, hyeongmin.gender))

## 257
"""
add method who() which prints name, age, gender
"""
class Human:
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender
  def who(self):
    print("name : {}, age = {}, gender = {}".format(self.name, self.age, self.gender))
hyeongmin = Human("Hyeongmin", 23, "male")
hyeongmin.who()

## 258
"""
add method setinfo() which updates name, age, gender
"""
class Human:
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender
  def who(self):
    print("name : {}, age = {}, gender = {}".format(self.name, self.age, self.gender))
  def setinfo(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

hyeongmin = Human("Unknown", 23, "Unknown")
hyeongmin.who()
hyeongmin.setinfo("Hyeongmin", 23, "male")
hyeongmin.who()

## 259
"""
add destructor which prints "Bye"
"""
class Human:
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender
  def __del__(self):
    print("Bye")
  def who(self):
    print("name : {}, age = {}, gender = {}".format(self.name, self.age, self.gender))
  def setinfo(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

hyeongmin = Human("Unknown", 23, "Unknown")
del(hyeongmin)

## 260
"""
describe why error occurs

class OMG: 
  def print():
    print("Oh my god")

myStock = OMG()
myStock.print()
"""
# need 'self' for print argument
# e.g. def print(self):
