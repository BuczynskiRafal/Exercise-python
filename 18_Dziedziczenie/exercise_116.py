class Container:
    pass


class TemperatureControlledContainer(Container):
    pass


class RefrigeratedContainer(TemperatureControlledContainer):
    pass


print(issubclass(TemperatureControlledContainer, Container))
print(issubclass(RefrigeratedContainer, TemperatureControlledContainer))
print(issubclass(RefrigeratedContainer, Container))