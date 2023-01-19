## 121
# flip upper/lower of input alphabet
user = input("one alphabet : ")
if user.islower():
  print(user.upper())
else:
  print(user.lower())
  
## 122
# get score from input, print grade
score = int(input("score : "))

if score > 80:
  print('A')
elif score > 60:
  print('B')
elif score > 40:
  print('C')
elif score > 20:
  print('D')
else:
  print('F')
  
## 123
# currency exchanger
trade = {
  'dollar' : 1167,
  'yen' : 1.096,
  'euro' : 1268,
  'yuan' : 171
}

user = input("input [money unit] : ")
money, unit = user.split(' ')
print(float(money) * trade[unit], "krw")

## 124
# print max value among three input number
num1 = int(input("num1 : "))
num2 = int(input("num2 : "))
num3 = int(input("num3 : "))

print(max(num1, num2, num3))
# or can implement by if statement

## 125
# from input phone number, print telecom
phone_num = input("phone : ")
telecom = phone_num.split('-')[0]

if telecom == "011":
  print("SKT")
elif telecom == "016":
  print("KT")
elif telecom == "019":
  print("LGU")
elif telecom == "010":
  print("Unknown")

## 126
# from mail number, determine state
user = input("mail address : ")
tag = user[0:3]

if tag in ["010", "011", "012"]:
  print("Gangbuk-gu")
elif tag in ["013", "014", "015"]:
  print("Dobong-gu")
elif tag in ["016", "017", "018", "019"]:
  print("Nowon-gu")
  
## 127
"""from resident registration number (RRN), determine sex RRN's 7th number indicates sex 
(1,3 for male / 2,4 for female)
"""
rrn = input("resident registration number : ")
idx = int(rrn.split('-')[1][0])

if idx == 1 or idx == 3:
  print("male")
elif idx == 2 or idx == 4:
  print("female")

## 128
"""from resident registration number (RRN), print birth place is Seoul or not. 
Among RRN's second half, 2nd, 3rd number indicates birth place.
(00-08 for seoul / 09-12 for busan)

RRN format : 1234567-1234567
"""
rrn = input("resident registration number : ")
code = rrn.split('-')[1][1:3]

if 0 <= int(code) <= 8:
  print("Seoul")
else:
  print("Not Seoul")
  
## 129
"""check validity of rrn.
last digit of rrn is the validation number,
which should equal to following result.

  8 2 1 0 1 0 - 1 6 3 5 2 1 0
x 2 3 4 5 6 7   8 9 2 3 4 5 
-----------------------------
1st : (8*2 + 2*3 + 1*4 + 0*5 + 1*6 + 0*7 + 1*8 + 6*9 + 3*2 + 5*3 + 2*4 + 1*5) = (128 % 11) = 7
2nd: 11 -7 = 4
"""
rrn = input("resident registration number : ")

result1 = int(rrn[0]) * 2 + int(rrn[1]) * 3 + int(rrn[2]) * 4 + int(rrn[3]) * 5 + int(rrn[4]) * 6 + int(rrn[5]) * 7 + int(rrn[7]) * 8 + int(rrn[8]) * 9 + int(rrn[9]) * 2 + int(rrn[10]) * 3 + int(rrn[11]) * 4 + int(rrn[12]) * 5

result2 = 11 - (result1 % 11)

if result2 == int(rrn[13]):
  print("Valid")
else:
  print("Error")
  
## 130
""" determine bull/bear market of the btc info
Key Name      |	Description
opening_price	| Starting price in recent 24h
closing_price	| Ending price in recent 24h
min_price	    | Min price in recent 24h
max_price	    | Max price in recent 24h
"""
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

open_price = float(btc['opening_price'])
diff_price = float(btc['max_price']) - float(btc['min_price'])
max_price = float(btc['max_price'])

if (open_price + diff_price) > max_price:
  print("Bull market")
else:
  print("Bear market")
