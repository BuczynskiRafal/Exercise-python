class Vector:

    def __init__(self, *args):
        self.components = args

    def __repr__(self):
        return f"{self.__class__.__name__}{self.components}"


v1 = Vector(-3, 4, 2)
print(v1)