## 021 : String Indexing
letters = 'python'
print(letters[0], letters[2])

## 022 : String Slicing
license_plate = "22가 2210"
print(license_plate[4:]) # license_plate[4] ~ end

## 023
# [st : en : offset]
string = "홀짝홀짝홀짝"
print(string[::2])

## 024
string = "PYTHON"
print(string[::-1])

## 025 : String Substitution
# using method 'replace'
phone_number = "010-1111-2222"
phone_number = phone_number.replace('-',' ')
print(phone_number)

## 026
phone_number = "010-1111-2222"
phone_number = phone_number.replace('-','');
print(phone_number)

## 027
# using split, extract domain
url = "http://sharebook.kr"
domain = url.split('.') #'http://sharebook', 'kr'
print(domain[1])

## 028
lang = 'python'
# lang[0] = 'P' # str object does not support item assignment
print(lang)

## 029
string = 'abcdfe2a354a32a'
string = string.replace('a','A')
print(string)

## 030
string = 'abcd'
string.replace('b','B')
print(string)
# still printing 'abcd'
# string does not changable.
# keep original, replace method returns new string object
