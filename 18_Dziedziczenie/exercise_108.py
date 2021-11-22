class Container:
    pass


class PlasticContainer(Container):
    pass


class MetalContainer(Container):
    pass


class SmallPlasticContainer(PlasticContainer):
    pass


print(SmallPlasticContainer.mro())