# Pytanie 40 - ciąg Fibonacciego to ciąg liczb, którego:
# - zerowy element wynosi 0
# - pierwszy element wynosi 1
# - każdy kolejny element jest sumą dwóch poprzedzających go elementów.
# Napisz funkcję, która zwróci n-ty element ciągu Fibonacciego.

# kolejny element ciągu: 0   1   2   3   4   5   6    7   8   9  10
# wartość dla elementu:  0   1   1   2   3   5   8   13  21  34  55

# def fibo(n):
#     first = 0
#     second = 1
#     for number in range(n-1):
#         first, second = second, first + second
#     return second


def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(10))
