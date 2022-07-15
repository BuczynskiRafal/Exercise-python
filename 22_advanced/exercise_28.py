def binary_to_int():
    with open('binary.txt', 'r') as file:
        numbers = file.readlines()
    return [int(number[:-1], 2) for number in numbers]


print(binary_to_int())
