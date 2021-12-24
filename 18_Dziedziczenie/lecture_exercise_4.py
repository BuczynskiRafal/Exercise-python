class Vehicle:

    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year


class Car(Vehicle):

    def __init__(self, brand, color, year, horsepower):
        super().__init__(brand, color, year)
        self.horsepower = horsepower


v1 = Vehicle('Tesla', 'red', 2020)

c1 = Car('Tesla', 'red', 2020, 300)


print(v1.__dict__)
print(c1.__dict__)
