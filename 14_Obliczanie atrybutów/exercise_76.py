class Rectangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._area = None

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width_val):
        self._width = width_val
        self._area = None

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height_val):
        self._height = height_val
        self._area = None

    @property
    def area(self):
        if self._area is None:
            self._area = self.height * self.width
        return self._area


rectangle = Rectangle(3, 4)
print(f"width: {rectangle.width}, height: {rectangle.height} -> area: {rectangle.area}")