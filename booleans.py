first = ""
last = ""
zero = False
empty_string = False
none = False
eqality = "== | != | > | < | >= | <="

if first == "ash" and last == "bash":
    print("name is equal to ashbash")
elif last == "bash":
    print("name is equal to bash")
elif first == "ash": 
    print("name is equal to ash")
elif first == "ashley" or last == "schultz":
    print("name is formal")
elif first:
    print("first name is not blank")
elif not last:
    print("last name is blank")
else:
    print("name is not set")

a = [1,2,3]
b = [1,2,3]
c = a 
if a is b:
    print("a and b are the same")
elif a is c:
    print("a and c are the same")
