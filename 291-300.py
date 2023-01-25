## 291
"""
write 'text1.txt' as follows
---
005930
005380
035420
"""
import os
print(os.getcwd())

f = open("/home/runner/Python-Practice/text1.txt", mode = "wt")
f.write("005930\n")
f.write("005380\n")
f.write("035420")
f.close()

## 292
"""
write 'text2.txt' as follows
---
005930 samsung
005380 hyundai
035420 NAVER
"""
f = open("/home/runner/Python-Practice/text2.txt", mode = "wt")
f.write("005930 samsung\n")
f.write("005380 hyundai\n")
f.write("035420 NAVER")
f.close()

## 293
"""
create 'stock.csv' and write as follows. 
Should use cp949 encoding

name    | code   | PER
samsung | 005930 | 15.79
hyundai | 005380 | 55.82
"""
import csv

f = open("/home/runner/Python-Practice/stock.csv", mode = "wt", encoding = 'cp949', newline = '')
writer = csv.writer(f)
writer.writerow(['name', 'code', 'PER'])
writer.writerow(['samsung', '005930', 15.79])
writer.writerow(['hyundai', '035420', 55.82])
f.close()

## 294
"""
read 'text1.txt' and save code to list
"""
f = open("/home/runner/Python-Practice/text1.txt")
lines = f.readlines()

codes = [line.strip() for line in lines]
print(codes)
f.close()

## 295
"""
read 'text2.txt' and save code, name as dictionary
"""
f = open("/home/runner/Python-Practice/text2.txt")
lines = f.readlines()

data = {}
for line in lines:
  line = line.strip() # remove '\n'
  key, val = line.split() # default : ' '
  data[key] = val

print(data)
f.close()

## 296
"""
converting 'str' type PER to float type.
when error occurs, you should print 0 
(exception handling)
"""
per = ["10.31", "", "8.00"]

for i in per:
  try:
    print(float(i))
  except:
    print(0)

## 297
"""
save value of #296 in list
"""
per = ["10.31", "", "8.00"]

list = []
for i in per:
  try:
    v = float(i)
  except:
    v = 0
  list.append(v)
print(list)

## 298
"""
implement division.
you should handle only ZeroDivisionError, not all exception
"""
try:
  a = 1/0
except ZeroDivisionError:
  print("zero division")

## 299
"""
practice exception binding with variable

try:
  (...)
except 'exception' as 'e':
  print(e)

try at list IndexError
"""
data = [1, 2, 3]
for i in range(5):
  try:
    print(data[i])
  except IndexError as e:
    print(f"{e} : {i}")

## 300
"""
use try, except, else, finally

try:
  (code)
except:
  (when exception occurs)
else:
  (when exception not occurs)
finally:
  (always run)
"""
per = ["10.31", "", "8.00"]

for i in per:
    try:
      print(float(i))
    except:
      print("error")
    else:
      print("clean data")
    finally:
      print("finished!")
