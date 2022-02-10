def is_prime(number: int) -> bool:
    n = 2
    if number < 2:
        return False
    while n * n <= number:
        if number % n == 0:
            return False
        n += 1
    return True


def calculate() -> int:
    counter = 1
    number = 0
    iterator = 1
    while counter < 100:
        if is_prime(iterator):
            number = iterator
            counter += 1
            iterator += 1
        iterator += 1
    return number

print(calculate())