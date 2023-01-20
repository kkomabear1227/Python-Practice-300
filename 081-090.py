## 081
"""
bind left 8 value to the valid_scores
"""
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_scores, _, _ = scores
print(valid_scores)

## 082
"""
bind right 8 value to the valid_scores
"""
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, _, *valid_scores = scores
print(valid_scores)

## 083
"""
bind middle 8 value to the valid_scores
"""
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, *valid_scores, _ = scores
print(valid_scores)

## 084
"""
create empty dictionary name 'tmp'
"""
tmp = {}

## 085
"""
create dictionary

apple : 1000
banana : 1200
kiwi : 1800
"""
ice_cream = {
  "apple" : 1000,
  "banana" : 1200,
  "kiwi" : 1800
}

## 086
"""
add following info to the #085's dictionary

mandarin : 1200
watermelon : 1500
"""
ice_cream['mandarin'] = 1200
ice_cream['watermelon'] = 1500
print(ice_cream)

## 087
"""
using #086's dictionary, print price of apple
"""
print(ice_cream['apple'])

## 088
"""
update apple's price to 1300
"""
ice_cream['apple'] = 1300
print(ice_cream['apple'])

## 089
"""
delete apple from dictionary
"""
del ice_cream['apple']
print(ice_cream)

## 090
"""
determine why error occurs
"""
# ice_cream['melon']
"""
Traceback (most recent call last):
  File "main.py", line 80, in <module>
    ice_cream['melon']
KeyError: 'melon'

indexing with non-existing key makes error
"""
