def calculate():
    numbers = [number for number in range(100, 1000) if str(number) == str(number)[::-1]]
    return len(numbers)

print(calculate())