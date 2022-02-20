# przy użyciu wyszukiwania binarnego sprawdź czy liczba 341 znajdusje się w posortowanej liście

P = [-10, -7, -5, -3, 0, 3, 5, 21, 68, 341, 500]


# szukana = 341       # liczba której szukam
# lewy = 0            # indeks lewy
# prawy = len(P)-1    # indeks prawy - długość pomnieszona o 1 ponieważ listy nają indeksy zaczynające się od 0
# while lewy <= prawy:                # wykonuje się dopuki lewa stona zakresu jest mniejsza niż prawa lub będą równe
#     srodek = (lewy + prawy) // 2    #tworzę indeks środkowy
#     if P[srodek] == szukana:
#         print(f"Liczba {szukana} znajduje się na liście.") # wypisz informację, że wartość znaleziono
#         break
#     elif P[srodek] < szukana:
#         lewy = srodek + 1
#     else:
#         if P[srodek] > szukana:
#             prawy = srodek - 1


# def binary_search(elements: list, search_value) -> bool:
#     left = 0
#     right = len(elements) -1
#     while left <= right:
#         center = (left + right) // 2
#         if elements[center] == search_value:
#             return True
#         elif elements[center] < search_value:
#             left = center + 1
#         else:
#             if elements[center] > search_value:
#                 right = center - 1


def binary_search(elements: list, search_value) -> bool:
    left = 0
    right = len(elements) -1
    for index in elements:
        center = (left + right) // 2
        if elements[center] == search_value:
            return True
        elif elements[center] < search_value:
            left = center + 1
        else:
            if elements[center] > search_value:
                right = center - 1
    return False


print(binary_search(elements=P, search_value=341))








# szukana = 100        # zmienna przechowująca szukaną wartość
# lewy = 0             # indeks lewy określający początek przeszukiwanego zakresu listy
# prawy = len(P) - 1   # indeks prawy określający koniec przeszukiwanego zakresu listy
# while lewy <= prawy: # dopóki indeks lewy jest mniejszy lub równy prawemu
#     srodkowy = (lewy + prawy) // 2  # wyliczamy indeks srodkowy, jako średnią indeksów lewy i prawy (// - zwraca część całkowitą z dzielenia)
#     if P[srodkowy] == szukana:  # jeśli lista od inseksu srodkowy zawiera szukaną wartość
#         print(f"Liczba {szukana} znajduje się na liście.") # wypisz informację, że wartość znaleziono
#         break        # i przerwij działanie pętli while
#     elif P[srodkowy] < szukana:  # jeśli lista od indeksu srodkowy zawiera wartość mniejszą niż szukana
#         lewy = srodkowy + 1      # przesuń indeks lewy na pozycję o jeden większą niz srodkowy
#     else:                        # w przeciwnym wypadku (czyli jeśli lista od indeku srodkowy zawiera wartość większa niż szukana)
#         prawy = srodkowy - 1     # przesuń indeks prawy na pozycję o jeden mniejszą niż srodkowy
# else:                 # jeśli pętla while skończy się wykonywać, bo warunek w niej zawarty zwróci False, to wtedy uruchomi się ten else
#     print(f"Liczby {szukana} nie ma na liście.")