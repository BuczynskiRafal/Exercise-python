class Model:
    pass


class View:
    pass


object1 = Model()
object2 = [Model(), Model()]
object3 = {}

print(isinstance(object1, (Model, View)))
print(isinstance(object2, (Model, View)))
print(isinstance(object3, (Model, View)))