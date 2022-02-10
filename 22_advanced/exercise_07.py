def calculate():
    numbers = [ x * y
                for x in range(10, 100)
                for y in range(10, 100)
                if str(x*y) == str(x*y)[::-1]]
    return max(numbers)

print(calculate())