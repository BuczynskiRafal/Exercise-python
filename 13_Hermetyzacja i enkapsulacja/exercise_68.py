class Pet:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


pet = Pet('Max', 5)
print(pet.__dict__)
pet.name = 'Tom'
pet.age = 8
print(pet.__dict__)
