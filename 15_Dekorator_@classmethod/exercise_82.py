class Person:
    instances = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Person.instances.append(self)

    @classmethod
    def count_instances(cls):
        return len(Person.instances)


p1 = Person(first_name="Romek", last_name="Tomek")
p2 = Person(first_name="Cezary", last_name="Cezary")

print(p2.count_instances())
