import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self._area = None

    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * self._radius * self._radius
        return self._area


circle = Circle(3)
print(round(circle.area, 4))
