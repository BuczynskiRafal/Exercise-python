from itertools import groupby


def compress(number):
    numbers = [ (key, len(list(group))) for key, group in groupby(str(number))]
    return numbers


print(compress(11123123))
