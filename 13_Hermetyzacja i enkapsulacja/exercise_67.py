class Pet:

    def __init__(self, name=None):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


pet = Pet('Max')
pet.name = 'Oscar'
print(pet.__dict__)