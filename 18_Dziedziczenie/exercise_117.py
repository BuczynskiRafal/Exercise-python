class Container:

    category = 'general purpose'


class TemperatureControlledContainer(Container):
    temp_range = (-25.0, 25.0)


class RefrigeratedContainer(TemperatureControlledContainer):
    temp_range = (-25.0, 5.0)


print(getattr(RefrigeratedContainer, 'temp_range'))
