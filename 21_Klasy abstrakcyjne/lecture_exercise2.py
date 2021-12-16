from abc import ABC, abstractmethod


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


figures = [Square(), Square(5), Square(10)]

for figure in figures:
    print(f"Side length: {figure.a}")
    print(f"Area: {figure.area()}")
    print(f"Perimeter: {figure.perimeter()}\n")
