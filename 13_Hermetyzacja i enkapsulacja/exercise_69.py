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
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int):
            if value >= 0:
                self._age = value
                return self._age
            else:
                raise ValueError('The value of age must be a positive integer.')
        else:
            raise TypeError('The value of age must be of type int.')

try:
    pet = Pet('Max', 'seven')
except TypeError as error:
    print(error)