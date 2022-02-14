def is_palindrome(number: int) -> bool:
    string_number = str(number)
    bin_number = str(bin(number))
    if not string_number == string_number[::-1] or bin_number == bin_number[::-1]:
        return False
    return True

print(is_palindrome(90))
