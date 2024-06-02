#!/usr/bin/python3
"""
Abstract base classes
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class for shapes."""
    @abstractmethod
    def area(self):
        """Abstract method to calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Class representing a circle."""
    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Class representing a rectangle."""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints the area and perimeter of the given shape."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
