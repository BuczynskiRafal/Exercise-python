class Pet:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name

    name = property(fget=name)


pet = Pet('Max')
print(pet.__dict__)