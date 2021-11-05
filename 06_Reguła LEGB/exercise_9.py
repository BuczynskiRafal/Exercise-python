def display_info(number_of_updates=1):
    counter = 100
    dot_counter = ""

    def update_counter():
        nonlocal counter, dot_counter
        counter += 1
        dot_counter += "."

    [update_counter() for _ in range(number_of_updates)]

    print(counter)
    print(dot_counter)


display_info(number_of_updates=10)