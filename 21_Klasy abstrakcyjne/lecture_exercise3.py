from abc import ABC, abstractmethod
import math


class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Figure):

    def __init__(self, a=1):
        self.a = a

    def area(self):
        return self.a ** 2

    def perimeter(self):
        return self.a * 4


class Circle(Figure):

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * math.pi

    def perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Figure):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = self.perimeter()/2
        a = p-self.a
        b = p-self.b
        c = p-self.c
        return math.sqrt(p * a * b * c)

    def perimeter(self):
        return self.a + self.b + self.c

figures = [Square(), Square(5), Square(10), Circle(), Circle(5), Circle(10), Triangle(1, 1, 1), Triangle(5, 5, 5), Triangle(10, 10, 10)]

for figure in figures:
    print(f"Area: {figure.area():.2f}.")
    print(f"Perimeter: {figure.perimeter():.2f}\n")
