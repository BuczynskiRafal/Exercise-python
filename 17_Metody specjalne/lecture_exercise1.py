class Integer:

    def __init__(self, integer=0):
        self.integer = int(integer)

    def __str__(self):
        return f'{self.integer}'

    def __repr__(self):
        return f'{self.integer}'

    def __add__(self, other):
        return Integer(self.integer + other.integer)

    def __sub__(self, other):
        return Integer(self.integer - other.integer)


i1 = Integer(5)
i2 = Integer(10)

print(i1.__add__(i2))