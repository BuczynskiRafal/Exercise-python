class Vehicle:

    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

    def display_attrs(self):
        for attr, value in self.__dict__.items():
            print(f'{attr} -> {value}')


class Car(Vehicle):

    def __init__(self, brand, color, year, horsepower):
        super().__init__(brand, color, year)
        self.horsepower = horsepower

    def display_attrs(self):
        print(f"Calling from class: {self.__class__.__name__}")
        super().display_attrs()


car = Car('Tesla', 'black', 2018, 260)
car.display_attrs()
