def is_palindrome(number):
    if str(number) != str(number)[::-1]:
        return False
    bin_number = bin(number)[2:]
    return bin_number == bin_number[::-1]


def calculate():
    numbers = [number for number in range(100, 1000) if is_palindrome(number)]
    return numbers


print(calculate())