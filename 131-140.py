## 131
# expect result
fruits = ['apple', 'mandarin', 'watermelon']
for fruit in fruits:
  print(fruit)

"""
apple
mandarin
watermelon
"""

## 132
# expect result
fruits = ['apple', 'mandarin', 'watermelon']
for fruit in fruits:
  print('#####')

"""
#####
#####
#####
"""

## 133
# disassemble for statement
"""
for val in ['A', 'B', 'C']:
  print(val)
"""
print('A')
print('B')
print('C')

## 134
# disassemble for statement
"""
for val in ['A', 'B', 'C']:
  print('output :', val)
"""
print('output :', 'A')
print('output :', 'B')
print('output :', 'C')

## 135
# disassemble for statement
"""
for val in ['A', 'B', 'C']:
  val = val.lower()
  print(val)
"""
val = 'A'
val = val.lower()
print(val)
val = 'B'
val = val.lower()
print(val)
val = 'C'
val = val.lower()
print(val)

## 136
# assemble to for statment
"""
val = 10
print(val)
val = 20
print(val)
val = 30
print(val)
"""

for val in [10, 20, 30]:
  print(val)

## 137
# assemble to for statment
"""
print(10)
print(20)
print(30)
"""
for val in [10, 20, 30]:
  print(val)

## 138
# assemble to for statment
"""
print(10)
print("-----")
print(20)
print("-----")
print(30)
print("-----")
"""
for val in [10, 20, 30]:
  print(val)
  print("-----")

## 139
# assemble to for statment
"""
print("+++++")
print(10)
print(20)
print(30)
"""
print("+++++")
for val in [10, 20, 30]:
  print(val)

## 140
# assemble to for statment
"""
print("-----")
print("-----")
print("-----")
print("-----")
"""
for i in range(4):
  print("-----")
