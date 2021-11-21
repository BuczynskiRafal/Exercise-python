class Laptop:
    brand = 'Lenovo'
    model = 'ThinkPad'


setattr(Laptop, 'brand', 'Acer')
setattr(Laptop, 'model', 'Predator')

print(f"brand: {getattr(Laptop, 'brand')}")
print(f"model: {getattr(Laptop, 'model')}")