arr = [{"name": "Ash", "age": 33, "hobby": "Programming"},
     {"name": "Bash", "age": 44, "hobby": "Drinking Tea"},
     {"name": "AshBash", "age": 55, "hobby": "Hiking"}]

nums = range(4,9) # [4,5,6,7,8]

includes = 5 in nums

for i in arr:
    print(f"Name: {i['name']}")
    print(f"Age: {i['age']}")
    print(f"Hobby: {i['hobby']}")
    print("-----------------------")

for i in nums:
     print(i)

msg = ""
while msg != "ashbash":
    msg = input("Enter the password")
    if msg == "exit":
        break
print("Awesome Possom!")

num = 0
while num < 10:
    print(num)
    num += 1
print("Awesome Possom!")

