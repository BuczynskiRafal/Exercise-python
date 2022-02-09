def calculate():
    first = 0
    second = 1
    sum_numbers = 0
    while second < 1000000:
        first, second = second, first + second
        if second % 2 == 0:
            sum_numbers += second
    return sum_numbers


print(calculate())
