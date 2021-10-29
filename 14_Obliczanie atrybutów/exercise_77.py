class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._area = None
        self._perimeter = None

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
        self._area = None
        self._perimeter = None

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
        self._area = None
        self._perimeter = None

    @property
    def area(self):
        if self._area is None:
            self._area = self._width * self._height
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = 2 * self._width + 2 * self._height
        return self._perimeter


rectangle = Rectangle(3, 4)
print(f"width: {rectangle.width}, height: {rectangle.height} -> perimeter: {rectangle.perimeter}")