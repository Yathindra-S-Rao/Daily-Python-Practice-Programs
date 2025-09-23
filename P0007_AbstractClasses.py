from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound():
        pass


class Dog(Animal):

    def sound():
        print("Bark")


class Cat(Animal):

    def sound():
        print("Moeu")


d1 = Dog.sound()
c1 = Cat.sound()
