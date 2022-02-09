def calculate():
    sum_numbers = 0
    for number in range(100):
        if number % 5 == 0 or number % 7 == 0:
            sum_numbers += number
    return sum_numbers


print(calculate())