## 011
# 한글도 변수명으로 사용할 수 있다.
samsung = 50000
print(samsung * 10)

## 012
market_cap = 298e12
current_price = 5e4
PER = 15.79

print(market_cap, type(market_cap))
print(current_price, type(current_price))
print(PER, type(PER))

## 013
s = "hello"
t = "python"

print(s + "!", t)
print(f"{s}! {t}")

## 014
print(2 + 2 * 3)

## 015
a = "132"
print(type(a))

## 016
num_str = "720"
print(num_str, type(num_str))
num_int = int(num_str)
print(num_int, type(num_int))

## 017
num_int = 100
print(num_int, type(num_int))
num_str = str(num_int)
print(num_str, type(num_str))

## 018
num_str = "15.79"
print(num_str, type(num_str))
num_float = float(num_str)
print(num_float, type(num_float))

## 019
year = "2022"
year_int = int(year)
print(year_int - 3)
print(year_int - 2)
print(year_int - 1)

## 020
price_per_month = 48584
month = 36
print(price_per_month * month)
