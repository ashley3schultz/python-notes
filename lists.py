nums = [1,2,3,4,5,6,7,8,9]
numbers = list(range(10))


#methods 
nums.clear() # clears the list
nums.append(9) # add 1 item to a list
nums.extend([10,11,12,13,14]) # add a list to anther list
nums.pop() # removes last item
nums.pop(1) # removes item at index arg
nums.remove(12) # removes item equal to argumant
nums.insert(1,12) # add arg2 to a list at index arg1
nums.index(12) # returns what index arg occures
nums.index(12,2) # returns what index arg1 occures starting at arg2
nums.count(12 # counts occurance of arg)
nums.sort() # sorts asc
" ".join(nums) # list to string
_copy = nums[start:end:step] # [:] all | [:2] <2 [2:] >2 | [2:4] >2&<4 [::2] inc 2 | [::-1] reverse

# list comprehention 
[n+1 for n in nums] #for loop for lists
[bool(n) for n in nums]
[str(n) for n in nums]
[n for n in nums if num % 2 == 0]
[n*2 if n % 2 == 0 else n/2 for n in nums]