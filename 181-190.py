## 181
"""
define list 'apart' by row
101 102
201 202
301 302
"""
apart = [["room 101", "room 102"], ["room 201", "room 202"], ["room 301", "room 302"]]
print(apart)

## 182
"""
define list 'stock' by column

start | end
100   |  80
200   | 210
300   | 330
"""
stock = [["start", 100, 200, 300], ["end", 80, 210, 330]]
print(stock)

## 183
"""
define dictionary 'stock' by column.
start/end : key
other : value

start | end
100   |  80
200   | 210
300   | 330
"""
stock = {
  "start" : [100, 200, 300],
  "end" : [80, 210, 330]
}
print(stock)

## 184
"""
make this table to dictionary 'stock'.
using date for key, other row's will be value of list type.

10/10 | 80 110 70 90
10/11 | 210 230 190 200
"""
stock = {
  "10/10" : [80, 110, 70, 90],
  "10/11" : [210, 230, 190, 200]
}
print(stock)

## 185
"""
print list like example

apart = [ [101, 102], [201, 202], [301, 302] ]
room 101
room 102
room 201
room 202
room 301
room 302
"""
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
  for col in row:
    print(f"room {col}")

## 186
"""
print list like example

apart = [ [101, 102], [201, 202], [301, 302] ]
room 301
room 302
room 201
room 202
room 101
room 102
"""  
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart[::-1]:
  for col in row:
    print(f"room {col}")

## 187
"""
print list like example

apart = [ [101, 102], [201, 202], [301, 302] ]
room 302
room 301
room 202
room 201
room 102
room 101
"""  
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart[::-1]:
  for col in row[::-1]:
    print(f"room {col}")

## 188
"""
print list like example

apart = [ [101, 102], [201, 202], [301, 302] ]
room 101
-----
room 102
-----
room 201
-----
room 202
-----
room 301
-----
room 302
-----
"""  
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
  for col in row:
    print(f"room {col}")
    print("-----")

## 189
"""
print list like example

apart = [ [101, 102], [201, 202], [301, 302] ]
room 101
room 102
-----
room 201
room 202
-----
room 301
room 302
-----
"""  
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
  for col in row:
    print(f"room {col}")
  print("-----")

## 190
"""
print list like example

apart = [ [101, 102], [201, 202], [301, 302] ]
room 101
room 102
room 201
room 202
room 301
room 302
-----
"""  
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
  for col in row:
    print(f"room {col}")
print("-----")
