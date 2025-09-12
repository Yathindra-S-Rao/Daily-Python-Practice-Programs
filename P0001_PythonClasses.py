# Program to demonstrate a class and objects

class Person:
    
    def __init__(self, name, age, city, pincode):
        self.name = name
        self.age = age
        self.city = city
        self.pincode = pincode
        
    def get_name(self):
        return self.name.title()
        
    def get_address(self):
        return f"{self.city.title()} - {self.pincode}"
        
if __name__=='__main__':
    name = input('Enter Name: ')
    age = int(input('Enter Age: '))
    city = input('Enter city: ')
    pincode = input('Enter Pincode: ')
    p1 = Person(name, age, city, pincode)
    print(p1.get_name())
    print(p1.get_address())
