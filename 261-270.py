## 261
"""
create empty class 'Stock'
"""
class Stock:
  pass

## 262
"""
create constructor which can get name and code for argument

e.g. samsung = Stock('samsung', '005930')
"""
class Stock:
  def __init__(self, name, code):
    self.name = name
    self.code = code
    
samsung = Stock('samsung', '005930')

## 263
"""
add method set_name() which can update 'name'
"""
class Stock:
  def __init__(self, name, code):
    self.name = name
    self.code = code
  def set_name(self, name):
    self.name = name  

samsung = Stock('unknown', '005930')
print(samsung.name)
samsung.set_name('samsung')
print(samsung.name)

## 264
"""
add method set_code() which can update 'code'
"""
class Stock:
  def __init__(self, name, code):
    self.name = name
    self.code = code
  def set_name(self, name):
    self.name = name  
  def set_code(self, code):
    self.code = code

samsung = Stock('samsung', '000000')
print(samsung.code)
samsung.set_code('005930')
print(samsung.code)

## 265
"""
add method get_name, get_code which returns 'name', 'code'
"""
class Stock:
  def __init__(self, name, code):
    self.name = name
    self.code = code
  def set_name(self, name):
    self.name = name  
  def set_code(self, code):
    self.code = code
  def get_name(self):
    return self.name
  def get_code(self):
    return self.code
    
samsung = Stock('samsung', '005930')
print(f"name : {samsung.get_name()}")
print(f"code : {samsung.get_code()}")

## 266
"""
fix constructor so that it can get per, pbr, dividend for argument
"""
class Stock:
  def __init__(self, name, code, per, pbr, dividend):
    self.name = name
    self.code = code
    self.per = per
    self.pbr = pbr
    self.dividend = dividend
  def set_name(self, name):
    self.name = name  
  def set_code(self, code):
    self.code = code
  def get_name(self):
    return self.name
  def get_code(self):
    return self.code

## 267
"""
with class defined in #266, create instance with this information.

name : samsung
code : 005930
per : 15.79
pbr : 1.33
dividend : 2.83
"""
samsung = Stock('samsung', '005930', 15.79, 1.33, 2.83)

## 268
"""
create set_per(), set_pbr(), set_dividend() method
"""
class Stock:
  def __init__(self, name, code, per, pbr, dividend):
    self.name = name
    self.code = code
    self.per = per
    self.pbr = pbr
    self.dividend = dividend
  def set_name(self, name):
    self.name = name  
  def set_code(self, code):
    self.code = code
  def get_name(self):
    return self.name
  def get_code(self):
    return self.code
  def set_per(self, per):
    self.per = per
  def set_pbr(self, pbr):
    self.pbr = pbr
  def set_dividend(self, dividend):
    self.dividend = dividend

## 269
"""
using method defined in #268, update per to 12.75
"""
samsung = Stock('samsung', '005930', 15.79, 1.33, 2.83)
print(samsung.per)
samsung.set_per(12.75)
print(samsung.per)

## 270
"""
according to list below, create 3 instance of 'Stock' and save in python list
"""
stock_list = []

samsung = Stock('samsung', '005930', 15.79, 1.33, 2.83)
stock_list.append(samsung)

hyundai = Stock('hyundai', '005380', 8.70, 0.35, 4.27)
stock_list.append(hyundai)

LG = Stock('LG', '066570', 317.34, 0.69, 1.37)
stock_list.append(LG)

for stock in stock_list:
  print(stock.get_name(), stock.get_code())
