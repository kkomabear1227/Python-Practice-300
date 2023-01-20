## 151
"""
print negative number in the list
"""
list = [3, -20, -3, 44]
for num in list:
  if num < 0:
    print(num)

## 152
"""
print number in the list which is multiple of 3.
"""
list = [3, 100, 23, 44]
for num in list:
  if num % 3 == 0:
    print(num)

## 153
"""
print number in the list which is multiple of 3 and smaller than 20.
"""
list = [13, 21, 12, 14, 30, 18]
for num in list:
  if num % 3 == 0 and num < 20:
    print(num)

## 154
"""
print string in the list which length >= 3.
"""
list = ["I", "study", "python", "language", "!"]
for str in list:
  if len(str) >= 3:
    print(str)

## 155
"""
print only upper character in the list.
"""
list = ["A", "b", "c", "D"]
for char in list:
  if char.isupper():
    print(char)

## 156
"""
print only lower character in the list.
"""
list = ["A", "b", "c", "D"]
for char in list:
  if char.islower():
    print(char)

## 157 (*)
"""
convert the first character to uppercase and output.
(not capitalize!)
"""
list = ['dog', 'caT', 'paRRot']
for elem in list:
  print(elem[0].upper() + elem[1:])

## 158
"""
remove extension in elem and output.
"""
list = ['hello.py', 'ex01.py', 'intro.hwp']
for elem in list:
  tmp = elem.split('.')
  print(tmp[0])

## 159
"""
print list elem which extension name is '.h'
"""
list = ['intra.h', 'intra.c', 'define.h', 'run.py']
for elem in list:
  tmp = elem.split('.')
  if tmp[-1] == 'h':
    print(elem)

## 160
"""
print list elem which extension name is '.h' or '.c'
"""
list = ['intra.h', 'intra.c', 'define.h', 'run.py']
for elem in list:
  tmp = elem.split('.')
  if tmp[-1] == 'h' or tmp[-1] == 'c':
    print(elem)
