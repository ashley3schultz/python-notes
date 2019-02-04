class User:

    allowed = ['Ash', 'Bash', 'AshBash']

    all = [] #class variable 

    @classmethod
    def list_all(cls):
        for u in cls.all:
            print(u.first)

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.all.append(self)

    def full_name(self):
        return f"{self.first} {self.last}" 

    def initials(self):
       return f"{self.first[0]}. {self.last[0]}."  

    def change_age(self):
        self.age += 1
        return self.age

    

user1 = User('Ash', 'Bash', 33)
user2 = User('Bash', 'Ashley', 34)
user2 = User('Ashley', 'Bashley', 35)

User.list_all()
print(user1.initials())
print(user1.full_name())
print(user1.change_age())

 # __init__ # overides pythone method
 # _name # private methode
 # __age # name mangling user__age 