class Pet:

    def __init__(self, name, age):
        self._name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError('The value of age must be of type int.')
        if not value > 0:
            raise ValueError('The value of age must be a positive integer.')
        self._age = value


pet = Pet('Max', 7)
try:
    pet.age = -10
except ValueError as error:
    print(error)