## 041
# upper method : make all alphabet to uppercase letter
str = "abC"
str = str.upper()
print(str) #ABC

## 042
# lower method : make all alphabet to lowercase letter
str = "abC"
str = str.lower()
print(str) #abc

## 043
# capitalize method : make string capitalize
str = "abC"
str = str.capitalize()
print(str) #Abc (C became c!)

## 044
# endswith method checks end of the string
file_name = "dummy.xlsx"
print(file_name.endswith('xlsx'))

## 045
file_name = "dummy.xls"
print(file_name.endswith(('xlsx',"xls"))) 
# should bind two or more parameter using parentheses

## 046
# startswith checks start of the string
file_name = '2020_보고서.xlsx'
print(file_name.startswith('2020'))

## 047
# split method split string based on parameter
a = "hello world"
a = a.split(' ') # or simply a.split()
print(a) #['hello', 'world']

## 048
ticker = "btc_krw"
ticker = ticker.split('_')
print(ticker) #['btc', 'krw']

## 049
date = "2023-01-17"
date = date.split('-')
print(date)

## 050
# rstrip method is weaker version of strip() method
# sweep out right whitespaces
data = '011227        '
print(data.rstrip()  )
