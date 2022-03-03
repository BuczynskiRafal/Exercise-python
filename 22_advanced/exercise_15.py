from itertools import groupby


def compress(number):
    number = str(number)
    groups = [(key, '.' * len(list(dot))) for key, dot in groupby(number)]
    joined = [''.join(group) for group in groups]
    return ''.join(joined)


print(compress(112222))