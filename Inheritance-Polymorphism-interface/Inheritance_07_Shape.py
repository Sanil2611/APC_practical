# Problem Statement:
# Create a base class Shape containing a method to display the name of the shape.
# Create three derived classes Circle, Rectangle, and Triangle. Each class should
# implement its own method to calculate the area.

import math

class Shape:
    def display_name(self, name):
        print("Shape:", name)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


c = Circle(7)
r = Rectangle(10, 5)
t = Triangle(10, 6)

c.display_name("Circle")
print("Area:", c.area())

r.display_name("Rectangle")
print("Area:", r.area())

t.display_name("Triangle")
print("Area:", t.area())
