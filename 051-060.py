## 051
movie_rank = ['dr.strange', 'split', 'lucky']

## 052
# append batman at the back of the list 'movie_rank'
movie_rank.append('batman')
print(movie_rank)

## 053
# insert superman btw 'dr.strange' and 'split'
# help(movie_rank.insert)
movie_rank.insert(1, 'superman')
print(movie_rank)

## 054
# remove 'lucky'
# help(movie_rank.remove)
movie_rank.remove('lucky')
print(movie_rank)

## 055
# remove 'split' and 'batman' using 'del'
# current : ['dr.strange', 'superman', 'split', 'batman']
del movie_rank[2]
del movie_rank[2] # 'batman' reindexed to 2
print(movie_rank)

## 056
# combine two lists
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

langs = lang1 + lang2
print(langs)

## 057
# print max, min among the list
nums = [1, 2, 3, 4, 5, 6, 7]
print(max(nums), min(nums))

## 058
# print sum of the list elements
nums = [1, 2, 3, 4, 5]
print(sum(nums))

## 059
# print number of elements in the list
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

## 060
# print avg of the list element
nums = [1, 2, 3, 4, 5]
# print(avg(nums)) # no avg method!
avg = sum(nums) / len(nums)
print(avg)
