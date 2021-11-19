def stick(*args):
    joined = [arg for arg in args if isinstance(arg, str)]
    return '#'.join(*args)


print(stick('sport', 'summer'))
print(stick(3, 5, 7))
print(stick(False, 'time', True, 'workout', [], 'gym'))