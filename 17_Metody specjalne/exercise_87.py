class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"{self.__class__.__name__}(fname='{self.first_name}', lname='{self.last_name}')"


person = Person('Mike', 'Smith')
print(person)