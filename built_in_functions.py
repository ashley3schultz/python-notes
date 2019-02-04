
# LAMBDAS
### unnamed function aka anonimous functions 
### always on line
var = lambda : print("something") # takes in no param
var1 = lambda a: a * a # takes in one param
var2 = lambda a,b: a * b # takes in two param

lis = [1,2,3,4,5]

# MAP & LAMBDA
multiply = list(map(lambda a: a * a, lis))  # itterates on lambda

#FILTER & LAMBDA
evens = list(filter(lambda a: a % 2 == 0,lis))

#ALL 
allofit = all([num % 2 == 0 for num in lis]) # TRUE or FALSE
# all(num % 2 == 0 for num in numbers)

#ANY 
anyofit = any([num % 2 == 0 for num in lis]) # TRUE or FALSE
# any(num % 2 == 0 for num in numbers)

# MIN & MAX
min(lis)
max(lis)

# SORTED (sorts non-destructuive)
nums = [1,5,7,3]
print(sorted(nums)) # v/s sort()

# REVERSED (sorts non-destructuive)
nums = [1,5,7,3]
print(reversed('string')) # v/s sort()

#LEN
len(lis) # get elngth of dict, list, tuples, sets
# 'string'.__len__() 
def .__len__(): # overrides the built in functions

# ABS - absolute number
abs(-3.4) # 3.4

# Fabs (import math) for floats
fabs(-3) # 3.0

# SUM 
sum(lis, 1) # secend is start arg

# ROUND 
round(3.566, 2) # 3.56

# ZIP
l1 = [1,2,3]
l2 = [4,5,6]
list(zip(l1,l2)) # [(1,4),(2,5),(3,6)]
dict(zip(l1,l2)) # {1:4,2:5,3:6)}
# stops at lesser value of two lists