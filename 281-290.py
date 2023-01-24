## 281
"""
create class 'Car' so that this code can be run

car = Car(2, 1000)
print (car.wheel)  // 2
print (car.price)  // 1000
"""
class Car:
  def __init__(self, wheel, price):
    self.wheel = wheel
    self.price = price

## 282
"""
create class 'Bicycle' which inherits class 'Car'
"""
class Bicycle(Car):
  pass

## 283
"""
modify class 'Bicycle' so that this code can be run

bicycle = Bicycle(2, 100)
print(bicycle.price) //100
"""
class Bicycle(Car):
  def __init__(self, wheel, price):
    self.wheel = wheel
    self.price = price

## 284
"""
modify class 'Bicycle' so that this code can be run

bicycle = Bicycle(2, 100, 'cheonlian')
print(bicycle.brand) // cheonlian
"""
class Bicycle(Car):
  def __init__(self, wheel, price, brand):
    super().__init__(wheel, price)
    self.brand = brand

bi = Bicycle(2, 100, 'cheonlian')
print(bi.price)
print(bi.brand)

## 285
"""
create class 'Truck' so that this code can be run

t = Truck(4, 1000)
t.info()
---
wheel : 4
price : 1000
"""
class Truck(Car):
  def __init__(self, wheel, price):
    super().__init__(wheel, price)
  def info(self):
    print(f"wheel : {self.wheel}")
    print(f"price : {self.price}")

t = Truck(4, 1000)
t.info()

## 286
"""
modify class 'Car' so that class 'Bicycle' can also use info() method
"""
class Car:
  def __init__(self, wheel, price):
    self.wheel = wheel
    self.price = price
  def info(self):
    print(f"wheel : {self.wheel}")
    print(f"price : {self.price}")

class Truck(Car):
  def __init__(self, wheel, price):
    super().__init__(wheel, price)

class Bicycle(Car):
  def __init__(self, wheel, price, brand):
    super().__init__(wheel, price)
    self.brand = brand

bi = Bicycle(2, 100, 'cheonlian')
bi.info()

## 287
"""
modify class 'Bicycle' so that info() method can also print brand.
"""
class Bicycle(Car):
  def __init__(self, wheel, price, brand):
    super().__init__(wheel, price)
    self.brand = brand
  def info(self):
    super().info()
    print(f"brand : {self.brand}")

bi = Bicycle(2, 100, 'cheonlian')
bi.info()

## 288
"""
predict the result.

class parent:
  def call(self):
    print("parent call")

class child(parent):
  def call(self):
    print("child call")

me = child()
me.call()
"""
# child call (method overriding)

## 289
"""
predict the result.

class parent:
  def __init__(self):
    print("parent created")

class child(parent):
  def __init__(self):
    print("child created")

me = child()
"""
# child created

## 290
"""
predict the result.

class parent:
  def __init__(self):
    print("parent created")

class child(parent):
  def __init__(self):
    print("child created")
    super().__init__()

me = child()
"""
# child created
# parent created
