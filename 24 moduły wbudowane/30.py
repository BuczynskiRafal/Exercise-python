import sys


if len(sys.argv) > 1:
    numbers = [int(num) for num in sys.argv[1:]]
    result = sum(numbers)/len(numbers)
    print(f'Average: {result:.4f}.')
else:
    print(f'No values were given.')