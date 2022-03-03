from itertools import groupby


def compress(number):
    number = str(number)
    elements = [(key, str(len(list(group)))) for key, group in groupby(number)]
    result = [''.join(element) for element in elements]
    return '_'.join(result)

print(compress(1112))
