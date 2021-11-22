class Person:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f"Person(fname='{self.fname}', lname='{self.lname}')"

    def __str__(self):
        return f"First name: {self.fname}\nLast name: {self.lname}"


person = Person('John', 'Doe')
print(person)