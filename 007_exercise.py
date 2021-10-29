"""
Implement a function that returns
the largest palindromic number formed
by the product of two-digit numbers.
"""


# def calculate():
#     numbers = []
#     for x in range(10, 100):
#         for y in range(10, 100):
#             palindrom = x * y
#             if str(palindrom) == str(palindrom)[::-1]:
#                 numbers.append(palindrom)
#     return max(numbers)
#
# print(calculate())


def calculate():
    return max([x * y
                for x in range(10, 100)
                for y in range(10, 100)
                if str(x * y) == str(x * y)[::-1]])


print(calculate())
