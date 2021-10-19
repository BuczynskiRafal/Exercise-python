"""
Implement a function that takes
a natural number as an argument
and returns the greatest prime
factor of that number.
"""


def calculate(number):
    factor = []
    divider = 2
    while divider * divider <= number:
        if not number % divider == 0:
            divider += 1
        else:
            number = number // divider
            factor.append(divider)
    if number > 1:
        factor.append(number)
    return max(factor)


print(calculate())
