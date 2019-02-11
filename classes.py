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

 class Drink:
    def __init__(self, name, klass):
        self.name = name
        self.klass = klass

    def __repr__(self):
        return "A {} named {}!".format(self.klass, self.name)

class Tea(Drink):
    def __init__(self, name, oxid, temp):
        super().__init__(name, "Tea")
        self.temp = temp
        self.oxid = oxid

    # @property
    # def type(self):
    #     return self.oxid
    #
    # @temp.setter
    # def temp(self, val):
    #     if val > 212:
    #         self.temp = 212
    #     elif val < 150:
    #         self.temp = 150
    #     else:
    #         self.temp = val

tea1 = Tea("Longjing", "Green", 170)
print(tea1.oxid, tea1.klass)
print(tea1.name)
print(tea1.temp)