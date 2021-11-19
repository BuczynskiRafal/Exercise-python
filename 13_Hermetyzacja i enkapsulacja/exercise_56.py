class Laptop:

    def __init__(self, price):
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, value):
        self._price = value
        return self._price


laptop = Laptop(3499)
print(laptop.get_price())
laptop.set_price(3999)
print(laptop.get_price())

