class Person:

    def __init__(self, first_name,last_name):
        self._first_name = first_name
        self._last_name = last_name

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, name):
        self._first_name = name

    def get_last_name(self):
        return self._last_name

    def set_last_name(self, name):
        self._last_name = name

    first_name = property(fget=get_first_name, fset=set_first_name)
    last_name = property(fget=get_last_name, fset=set_last_name)


person = Person('John', 'Dow')
person.set_first_name('Tom')
person.set_last_name('Smith')
print(person.first_name)
print(person.last_name)
print(person.__dict__)