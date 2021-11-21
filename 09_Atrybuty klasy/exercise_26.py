class Phone:
    brand = 'Apple'
    model = 'iPhone X'


print(getattr(Phone, 'brand'))
print(getattr(Phone, 'model'))