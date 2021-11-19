class Person:

    def __init__(self, first_name):
        self._first_name = first_name

    def get_first_name(self):
        return self._first_name

    first_name = property(fget=get_first_name)


person = Person('John')
print(person.first_name)