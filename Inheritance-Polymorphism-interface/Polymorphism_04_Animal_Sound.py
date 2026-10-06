# Problem Statement:
# Create a base class Animal with a method sound(). Create subclasses Dog, Cat, Cow,
# and Lion. Override sound() in each class to display the appropriate sound.

class Animal:
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Woof")


class Cat(Animal):
    def sound(self):
        print("Meow")


class Cow(Animal):
    def sound(self):
        print("Moo")


class Lion(Animal):
    def sound(self):
        print("Roar")


animals = [Dog(), Cat(), Cow(), Lion()]

for animal in animals:
    animal.sound()
