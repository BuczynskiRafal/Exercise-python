V = ['Berlin', 'Paris', 'Rome', 'Madrid', 'Warsaw', 'Praque', 'Wien']
E = [ ('Madrid', 'Paris'),
    ('Paris', 'Berlin'),
    ('Berlin', 'Warsaw'),
    ('Warsaw','Praque'),
    ('Praque', 'Wien'),
    ('Wien', 'Rome'),
    ('Berlin', 'Wien'),
    ('Rome', 'Praque'),
    ('Praque', 'Warsaw')
]

city = 'Berlin'
cit = 'Warsaw'
# What can be next step when starting in Berlin?
def find_city(city: str, E: list, V:list) -> list:
    cities = [stop for start, stop in E if start == city]
    return cities

# To travel to Warsaw I can start my trip in...
def find_return(city: str, E: list, V:list) -> list:
    cities = [start for start, stop in E if stop == city]
    return cities


print(find_city(city, E, V))
print(find_return(cit, E, V))