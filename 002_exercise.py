"""
Find the numbers_sum of all the numbers divisible by 5 and 7 smaller than 100
"""
# numbers_sum = 0
# for number in range(0, 100):
#     if number % 5 == 0 or number % 7 == 0:
#         numbers_sum += number
#     print(numbers_sum)


# def calculate():
#     numbers_sum = 0
#     for number in range(0, 100):
#         if number % 5 == 0 or number % 7 == 0:
#             numbers_sum += number
#     return numbers_sum


def calculate():
    return sum([num for num in range(0, 100) if num % 5 == 0 or num % 7 == 0])


print(calculate())
