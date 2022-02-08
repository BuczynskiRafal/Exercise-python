class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Department:

    def __init__(self, dept_name, short_dept_name):
        self.dept_name = dept_name
        self.short_dept_name = short_dept_name


class Worker(Person, Department):

    def __init__(self, first_name, last_name, age, dept_name):
        Person.__init__(self, first_name, last_name, age)
        Department.__init__(self, dept_name)


print(Worker.mro())
