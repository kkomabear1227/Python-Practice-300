## 071
# create empty tuple
my_variable = ()
#print(type(my_variable)) # <class 'tuple'>

## 072
# create tuple
movie_rank = ('Dr.strange', 'split', 'lucky')
print(movie_rank)

## 073
# create tuple with one element (1)
my_tuple = (1)
print(type(my_tuple)) # <class 'int'>
my_tuple2 = (1,)
print(type(my_tuple2)) # <class 'tuple'>

## 074
# find reason for error
t = (1, 2, 3)
#t[0] = 'a'
# Ans : tuple is immutable

## 075
# what is type of t?
t = 1, 2, 3, 4
print(type(t)) # <class 'tuple'>
# for convenience, we can define tuple w/o parentheses

## 076
# modify t to ('A', 'b', 'c')
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')
print(t)

""" as saw in 074, we can not item assign to tuple 't'.
instead, create new tuple and update 't'.
('a', 'b', 'c') will automatically removed.
"""

## 077
# convert tuple to list
interest = ('Samsung', 'LG', 'SK Hynix')
interest2 = list(interest)
print(interest2)
#print(type(interest2))

## 078
# convert list to tuple
interest = ['Samsung', 'LG', 'SK Hynix']
interest2 = tuple(interest)
print(interest2)
#print(type(interest2))

## 079
# predict the result
tmp = ('apple', 'banana', 'cake')
a, b, c = tmp
print(a, b, c) # a = apple, b = banana, c = cake

## 080
# generate tuple with even number range from 1 ~ 99
#help(range)
""" range(st, en, step) : [st, en) range, generate number with stepsize 'step'
"""
data = tuple(range(2, 100, 2))
print(data)
