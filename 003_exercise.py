"""
Find the sum of all even expressions
of the Fibonacci sequence
less than 1000000.
"""


# def find_less_than_a_million():
#     fibo_even = []
#     start = 0
#     step = 1
#     while start < 1000000 or step < 1000000:
#         start, step = step, start + step
#         if step % 2 ==0:
#             fibo_even.append(step)
#     return sum(fibo_even)


def find_less_than_a_million():
    total = 0
    start = 0
    step = 1
    while start < 1000000 or step < 1000000:
        start, step = step, start + step
        if start % 2 == 0:
            total += start
    return total


print(find_less_than_a_million())
