# Program to demonstrate a classes, objects and Inheritance

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


class Personal(Person):

    def __init__(self, name, age, city, pincode, gender, phone):
        # Call parent class constructor
        super().__init__(name, age, city, pincode)
        self.gender = gender
        self.phone = phone

    def get_details(self):
        return f"Name: {self.get_name()}, Age: {self.age}, Gender: {self.gender}, Phone: {self.phone}, Address: {self.get_address()}"


if __name__ == '__main__':
    name = input('Enter Name: ')
    age = int(input('Enter Age: '))
    city = input('Enter City: ')
    pincode = input('Enter Pincode: ')
    gender = input('Enter Gender: ')
    phone = input('Enter Phone: ')

    p1 = Personal(name, age, city, pincode, gender, phone)

    print("\n--- Person Details ---")
    print(p1.get_details())