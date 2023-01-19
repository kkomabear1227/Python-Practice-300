## 061
# this list contains date and price info. print only price
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

## 062
# print only odd number
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2]) # idx 0 to end, hop by 2

## 063
# print only even number
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

## 064
# print list in reverse order
nums = [1, 2, 3, 4, 5]
print(nums[::-1]) # hop by -1 (backward)

## 065
# print only 'samsung' and 'naver'
interest = ['Samsung', 'LG', 'Naver']
print(interest[0], interest[2])

## 066
# using join method, print all list
# syntax : 'seperator'.join(list_name)
interest = ['Samsung', 'LG', 'Naver', 'SK Hynics']
# help(interest.join) # this is invalid syntax
print(' '.join(interest))

## 067
# insert '/' btw list elem while printing.
interest = ['Samsung', 'LG', 'Naver', 'SK Hynics']
print('/'.join(interest))

## 068
# print list element one by one. (one element in one line)
interest = ['Samsung', 'LG', 'Naver', 'SK Hynics']
print('\n'.join(interest))

## 069
# seperate string into list.
string = "Samsung/LG/Naver"
#help(string.split)
list = string.split('/')
print(list)

## 070
# sort list
data = [2, 4, 3, 1, 5, 10, 9]

# version 1. use sorted() function
data2 = sorted(data)
print(data2)

# version 2. use sort() method
#help(data.sort)
data.sort()
print(data)
