def is_prime(number: int) -> bool:
    n = 2
    if number < 2:
        return False
    while n * n <= number:
        if number % n == 0:
            return False
        n += 1
    return True


print(is_prime(0))