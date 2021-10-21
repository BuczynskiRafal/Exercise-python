"""
Implement a function that returns
the number of all three-digit
palindromic numbers.
"""


def calculate():
    count = 0
    for i in range(100, 1000):
        if str(i) == str(i)[::-1]:
            count += 1
    return count


print(calculate())
