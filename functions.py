from random import random
def coin():
    if random() > 0.5:
        return "Heads"
    else:
        return "Tails"

print(coin())

def greeting(name="You",greet_type="Hey"):
    return f"{greet_type} {name}!" 

print(coin())

n = input("What's you name")
g = input("How would you like to be greeted")

def blank()

print(greeting(greet_type=g, name=n))

#Scope

number = 5 # global scope

def count():
    global number #define global if changing the global variable
    number += 1
    return number

def outer():
    letters = 'a' # non local scope
    def inner():
        nonlocal letters
        letters += 'b'
        return letters
    return inner()

def simple1(arg):
    """docs for functon""" # adds a doc string to function
    return arg

def lots_of_args(*args): # use for any number of args
    total = 0
    for num in args: # = to a tuple
        total += num
    return total

    def lots_of_kv(*kwargs): # use for any number of key value args
    return kwargs # = to a dict simple
    # lots_of_kv(name="AshBash", age=33)

    # funcation param order 
    # 1. parametor (name)
    # 2. *args (name, *args)
    # 3. default params (name, *args, happy=true)
    # 4. **kwargs (name, *args, happy=true, **kwargs)

# sending list into (*args) params
my_list = [1,2,3,4,5,6]
lots_of_args(*my_list) # unpacks list into indevidual arguments

# sending dict into (**kwargs) params
my_dict = {'name':'Ash','Age':33}
lots_of_args(**my_dict) # unpacks dict into indevidual arguments