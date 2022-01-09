def fizz_buzz(n):
    for _ in range(1, n+1):
        if _ % 3 == 0 and _ % 5 == 0:
            print('FizzBuzz')
        elif _ % 5 == 0:
            print('Buzz')
        elif _ % 3 == 0:
            print('Fizz')
        else:
            print(_)


print(fizz_buzz(31))