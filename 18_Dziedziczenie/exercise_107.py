class Container:
    pass


class PlasticContainer(Container):
    pass


class MetalContainer(Container):
    pass


class CustomContainer:
    pass

print(issubclass(PlasticContainer, Container))
print(issubclass(MetalContainer, Container))
print(issubclass(CustomContainer, Container))