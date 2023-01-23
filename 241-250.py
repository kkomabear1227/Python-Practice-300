## 241
"""
using module 'datetime', print current time
"""
import datetime

now = datetime.datetime.now()
print(now)

## 242
"""
print type of now
"""
print(type(now))

## 243
"""
using timedelta in module 'datetime', print 5, 4, 3, 2, 1 day before today's time.
"""
#print(help(datetime.timedelta))
for day in range(-5, 0, 1):
  delta = datetime.timedelta(days = day)
  print(now + delta)

## 244
"""
print time like example. 

18:35:01

hint) use strftime method
"""
#import datetime # it seems like re-importing available
#print(help(datetime.datetime.strftime))
print(now.strftime('%H:%M:%S'))

## 245
"""
convert string '2023-01-23' to datetime.datetime type 
hint) use strptime() method in datetime.datetime
"""
day = '2023-01-23'
now = datetime.datetime.strptime(day, '%Y-%m-%d')
print(now, type(now))

## 246
"""
using time module and datetime module, print time in 1 second period.
"""
import time
import datetime

for i in range(5):
  now = datetime.datetime.now()
  print(now)
  time.sleep(1)

## 247
"""
describe 4 ways of module importing

https://www.pythonmorsels.com/4-ways-import-module-python/

1. import whole module
-> import math

2. import specific things from a module
-> from math import pi

3. avoid collision
from math import sqrt
from cmath import sqrt as csqrt

4. import module under different name
-> import math as m
"""

## 248
"""
using os module's getcwd(), print current directory
"""
import os
dir = os.getcwd()
print(dir)

## 249
"""
create 1.txt in directory, using os module's rename(), change its name to 2.txt
"""
os.rename("/home/runner/python-practice/1.txt", "/home/runner/python-practice/2.txt")

## 250
"""
using arange() in numpy module, print 0.0 to 5.0 with 0.1 inc
"""
import numpy as np 
for i in np.arange(0, 5, 0.1):
  print(i)
