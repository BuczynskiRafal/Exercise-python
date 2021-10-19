"""
Implement a function that takes a natural number as an argument
and returns a list containing the decomposition of this number
into prime factors.
"""

def calculate(num):
    number = []
    divider = 2
    while num >1:
        if num % divider == 0:
            num = num / divider
            number.append(divider)
        else:
            dzielnik += 1
    return number

print(calculate(10))