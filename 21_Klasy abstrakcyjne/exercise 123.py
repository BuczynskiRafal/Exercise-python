from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def area():
        pass


class Square(Figure):

    def ___init___(self, lenght):
        self.lenght = lenght

    def area(self, lenght):
        return lenght ** 2


try:
    figure = Figure()
except TypeError as e:
    print(e)