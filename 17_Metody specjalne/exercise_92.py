class Vector:

    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f'Vector{self.components}'

    def __str__(self):
        return f'{self.components}'

    def __len__(self):
        return len(self.components)

    def __bool__(self):
        if self.components[0] == 0:
            return False
        return True


v1 = Vector()
v2 = Vector(3, 2)
v3 = Vector(0, -3, 2)
v4 = Vector(5, 0, -1)

print(bool(v1))
print(bool(v2))
print(bool(v3))
print(bool(v4))
