# Problem Statement:
# Create an abstract class Shape with an abstract method area(). Derive Circle, Rectangle,
# and Triangle classes and implement the area() method for each shape. Create objects of
# the derived classes and display their areas.

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


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


shapes = [Circle(7), Rectangle(10, 5), Triangle(10, 6)]

for shape in shapes:
    print("Area:", shape.area())
