## 031 : Merge Strings
a = "3"
b = "4"
print(a + b) #34

## 032 : Multiply String
print("Hi" * 3) #HiHiHi

## 033
print('-' * 80)

## 034
t1 = 'python'
t2 = 'java'
print((t1 + ' ' + t2 + ' ') * 3)

## 035
# one way to print variable in python, %
name1 = "민수"
age1 = 10
name2 = "형민"
age2 = 23
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))

## 036
# another way to print variable in python, format method
name1 = "민수"
age1 = 10
name2 = "형민"
age2 = 23
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))

## 037
# print variable using f"" string
name1 = "민수"
age1 = 10
name2 = "형민"
age2 = 23
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

## 038
stock = "5,969,782,550"
stock = stock.replace(',',"")
stock = int(stock)
print(stock, type(stock))

## 039
period = "2020/30(E) (IFRS연결)"
print(period[:7])    #it seems like [st:en)

## 040
# we can sweep out left/right whitespace using strip() method
data = "   삼성전자   "
data = data.strip()
print(data)
