# Pytanie 33 - do czego w Pythonie służy słowo kluczowe yield ?
# Napisz przykładowy kod wykorzystujący yield.

def gen():
    for number in range(10):
        yield number

# numbers = gen()
# for num in numbers:
#     print(num)

symbols = '?><+_%^&*()'

values = (ord(symbol) for symbol in symbols)

for _ in range(15):
    print(next(values))