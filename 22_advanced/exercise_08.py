def greatest_common_divisor(num1:int, num2:int) -> int:
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


print(greatest_common_divisor(32, 48))