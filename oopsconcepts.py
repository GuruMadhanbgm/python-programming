import math
from abc import ABC, abstractmethod


# Abstract base class
class Shapes(ABC):

    @abstractmethod
    def find_area(self):
        pass

    @abstractmethod
    def display_area(self):
        pass


# Circle class
class Circle(Shapes):
    def __init__(self):
        self.radius = 3
        self.area = 0

    def find_area(self):
        self.area = math.pi * self.radius * self.radius

    def display_area(self):
        return self.area


# Triangle class
class Triangle(Shapes):
    def __init__(self):
        self.base = 5
        self.height = 4
        self.area = 0

    def find_area(self):
        self.area = 0.5 * self.base * self.height

    def display_area(self):
        return self.area


# Rectangle class
class Rectangle(Shapes):
    def __init__(self):
        self.length = 6
        self.breadth = 4
        self.area = 0

    def find_area(self):
        self.area = self.length * self.breadth

    def display_area(self):
        return self.area


# Object creation
c = Circle()
t = Triangle()
r = Rectangle()

# Finding and displaying areas
c.find_area()
print("Circle Area:", c.display_area())

t.find_area()
print("Triangle Area:", t.display_area())

r.find_area()
print("Rectangle Area:", r.display_area())
