class Vehicle:

    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year


class Car(Vehicle):

    def __init__(self, brand, color, year, horsepower):
        self.brand = brand
        self.color = color
        self.year = year
        self.horsepower = horsepower


vehicle = Vehicle('Tesla', 'red', 2020)
car = Car('Tesla', 'red', 2020, 300)

print(vehicle.__dict__)
print(car.__dict__)