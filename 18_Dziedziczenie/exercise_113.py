class Vehicle:

    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year


    def display_attrs(self):
        for attr, val in self.__dict__.items():
            print(f"{attr} -> {val}")

class Car(Vehicle):

    def __init__(self, brand, color, year, horsepower):
        super().__init__(brand, color, year)
        self.horsepower = horsepower


car = Car('Opel', 'black', 2018, 160)
car.display_attrs()