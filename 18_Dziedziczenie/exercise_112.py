class Vehicle:

    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year


class Car(Vehicle):

    def __init__(self, brand, color, year, horsepower):
        super().__init__(brand, color, year)
        self.horsepower = horsepower


vehicle = Vehicle('Tesla', 'red', 2020)
print(vehicle.__dict__)

car = Car('Tesla', 'red', 2020, 300)
print(car.__dict__)