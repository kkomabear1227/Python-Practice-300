## 161
"""
print 0 to 99
"""
for i in range(100):
  print(i)
  
## 162
"""
print worldcup year from 2002 to 2050. (4 year period)
"""
for year in range(2002, 2051, 4):
  print(year)
  
## 163
"""
print multiple of 3 range from 1 to 30.
"""
for i in range(3, 31, 3):
  print(i)

## 164
"""
print 99 to 0, 1 dec
"""
for i in range(100):
  print(99 -i)
  
## 165
"""
print like example
0.0 
0.1
(...)
0.9
"""
for i in range(10):
  print(i/10)

## 166
"""
print multiplication table of 3.
3x1 = 3
(...)
3x9 = 27
"""
for i in range(1,10):
  print(f"3x{i} = {3*i}")

## 167
"""
print odd multiplication table of 3.
3x1 = 3
3x3 = 9
(...)
3x9 = 27
"""
for i in range(1,10,2):
  print(f"3x{i} = {3*i}")

## 168
"""
sum 1 to 10 using for statment.
"""
sum = 0
for i in range(1,11):
  sum += i
print(sum)

## 169
"""
sum odd number range from 1 to 10 using for statment
"""
sum = 0
for i in range(1,11,2):
  sum += i
print(sum)

## 170
"""
multiply 1 to 10 using for statment
"""
mul = 1
for i in range(1,11):
  mul *= i
print(mul)
