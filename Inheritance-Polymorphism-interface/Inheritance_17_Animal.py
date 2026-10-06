# Problem Statement:
# Create a base class Animal with common attributes and methods. Derive Dog, Cat,
# and Cow classes and implement their specific sounds and behaviors.

class Animal:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Animal:", self.name)


class Dog(Animal):
    def sound(self):
        print("Dog says: Woof")


class Cat(Animal):
    def sound(self):
        print("Cat says: Meow")


class Cow(Animal):
    def sound(self):
        print("Cow says: Moo")


animals = [Dog("Tommy"), Cat("Kitty"), Cow("Gauri")]

for animal in animals:
    animal.display()
    animal.sound()
