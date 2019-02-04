d1 = {"name": "Ash", "age": 33, "hobby": "Programming"}
d2 = dict(name='ash',age=33,hobby='programming')

print(d1,d2)

for v in d1.values():
    print(v)

for k in d1.keys():
    print(k)

for k,v in d1.items():
    print(k+":",v)

# key exists
"name" in d1 # True
"job" in d1 # False

# key values
"ash" in d1.values() # True
"developer" in d1.values() # False

#methods
d1.copy() #creates a exact copy
dict.fromkeys("abc",0) #sets every value to arg2 or create new dict
d1.pop('name') # removes item arg
d1.get('name') # retrieves the arg value
d1.popitem() # removes random item - no args
d1.update(d2) # copies - d2 overwrites d1 and add others
# d1.clear() # clears the dict


# Dictionary Comrehention
l1 = ['a','b','c']
l2 = [1,2,3]
{k:v for k,v in d1.items()} #for loop for dict
print({l1[i]: l2[i] for i in range(len(l1))})