counter = 0
dot_counter = ""


def update_counter():
    global counter, dot_counter
    counter += 1
    dot_counter += "."


for _ in range(40):
    update_counter()
print(counter)
print(dot_counter)
