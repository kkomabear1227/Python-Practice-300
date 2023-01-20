## 191
"""
suppose tax rate 0.014%, calculate total price
using 2d list 'data'

print one price per oneline
"""
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

for row in data:
  for col in row:
    print(col * (1 + 0.014 * 0.01))

## 192
"""
add seperator "-----" per one row
"""
for row in data:
  for col in row:
    print(col * (1 + 0.014 * 0.01))
  print("-----")

## 193
"""
record output in 1d list 'result'
"""
result = []
for row in data:
  for col in row:
    price = col * (1 + 0.014 * 0.01)
    result.append(price)

print(result)

## 194
"""
record result in 2d list by row
"""
result = []
for row in data:
  result_row = []
  for col in row:
    price = col * (1 + 0.014 * 0.01)
    result_row.append(price)
  result.append(result_row)
print(result)

## 195
"""
list 'olhc' records price 'open', 'low', 'high', close'
print only 'close' price
"""
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for row in ohlc[1:]:
  print(row[-1])

## 196
"""
list 'olhc' records price 'open', 'low', 'high', close'
print only 'close' price if it is larger than 150
"""
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for row in ohlc[1:]:
  if row[-1] > 150:
    print(row[-1])

## 197
"""
list 'olhc' records price 'open', 'low', 'high', close'
print only 'close' price if 'close' >= 'open'
"""
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for row in ohlc[1:]:
  if row[-1] >= row[0]:
    print(row[-1])

## 198
"""
list 'olhc' records price 'open', 'low', 'high', close'
record diff('high' - 'low') in list 'volatiltiy'
"""
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

volatility = []
for row in ohlc[1:]:
  volatility.append(row[1] - row[2])
print(volatility)

## 199
"""
list 'olhc' records price 'open', 'low', 'high', close'
print diff('high' - 'low') if 'close' > 'open'
"""
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for row in ohlc[1:]:
  if (row[3] > row[0]):
    print(row[1] - row[2])

## 200
"""
list 'olhc' records price 'open', 'low', 'high', close'.
assume that player buys in 'open' price and sells 'close' price, calculate total profit.
"""
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

profit = 0
for row in ohlc[1:]:
  profit += row[3] - row[0]
print(profit)
