# Tuples
### like a list but cannot be changed
### you can use tuples as a key in dict - not lists
### loop over the same as a dict
numbers = (1,2,3,4,5)
first_one = numbers[0]
# Mehods 
numbers.count(1) #counts the instances of arg
numbers.index(1) #show the tuple index of arg


# Sets
### formal mathamatical sets
### collection of data with no dupplicate value
### group with no order
letters = {'a','b','c','d','e'}
nums = set({1,2,3,3,3}) # {1,2,3}
# Mehods 
'a' in letters # True
letters.add('g')
letters.remove('a')
letters.discard('b')
new_list = letter.copy()
new_list.clear()
combined = nums | letters # outer joins
in_both = nums | letters # inner joins
# Set Comprehention
{i+1 for i in range(3)}