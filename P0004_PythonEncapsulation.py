class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age 

    def get_age(self):  
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age

p = Person("Alice", 30)
print(p.name)           
# print(p.__age)        ---- Returns error
print(p.get_age())  

p.set_age(35)
print(p.get_age())  
