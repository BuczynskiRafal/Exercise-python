"""
Drukarka 1 drukuje 50 stron na każde 10 minut,
a drukarka 2 drukuje 50 stron na każde 30 minut.
Ile minut zajmie wydrukowanie 100 stron,
jeśli użyjesz 1 i 2 równocześnie?
"""


def time():
    d1 = 50 / (10*60)        # sekundy
    d2 = 50 / (30*60)        # sekundy
    ile_czasu_100 = 100 / (d1 + d1)
    print(ile_czasu_100/60)

time()