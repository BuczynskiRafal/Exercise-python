import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

EMAIL_FILE = BASE_DIR / 'email-Eu-core.txt'
FLIGHT_FILE = BASE_DIR / 'usa-domestic-flight-2019.csv'


def add_node(V, node):
    if node in V:
        return
    else:
        V[node] = {}


def add_edge(V, source, dest, weight):
    if not source in V.keys():
        add_node(V, source)
    if not dest in V.keys():
        add_node(V, dest)
    if not dest in V[source].keys():
        V[source][dest] = weight
    else:
        V[source][dest] += weight

V = {}
with open(EMAIL_FILE, 'r') as file:
    for line in file:
        u, v = line.split(' ')
        u = int(u)
        v = int(v)
        add_edge(V, u, v, 1)

# print(V)


import csv
from operator import itemgetter

network = {}
select_month = 1

with open(FLIGHT_FILE, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            line_count += 1
            origin = row[8]
            destination = row[11]
            month = int(row[12])

            if month != select_month:
                continue
            if origin not in network.keys():
                network[origin] = [destination]
            else:
                if destination not in network[origin]:
                    network[origin].append(destination)



# 7. No to mamy już wczytaną zawartość grafu! Jak chcesz możesz go wyświetlić (taaa na pewno
# wszystko się zmieści na ekranie), albo chociaż wyświetlić informację o liczbie przetworzonych
# wierszy:
print(f'Processed {line_count} lines.')

# 8. Dla wygody przetwarzania danych utwórz listę out_degrees, która będzie przechowywać nazwę
# miasta/lotniska oraz liczbę wychodzących z tego lotniska połączeń. Elementami tej listy może
# być słownik o dwóch kluczach: „name” określającym nazwę lotniska i „connections”
# przechowującym liczbę miast/lotnisk do których można wylecieć z tego lotniska.
out_degrees = [{'name': origin, 'connections': len(destinations) } for origin, destinations in network.items()]




# 9. Wariant prostszy – znajdź miasto/lotnisko z największą liczbą połączeń – to na tyle proste, że nie
# umieszczam dalszych instrukcji ;)
# 10. Wariant trudniejszy – poszukamy 10 najbardziej skomunikowanych lotnisk. Korzystając z funkcji
# sorted posortuj listę słowników out_degrees w kolejności malejącej (parametr reverse), ale
# uwaga… sortowanie ma się odbyć po wartości słownika wskazywanej przez „connections”, ale
# sortowane mają być całe słowniki z listy… I tutaj z pomocą przychodzi argument key, który
# powinien wskazywać na itemgetter('connections'). Wynik zapisz w top10:
max_degrees = max([airport['connections'] for airport in out_degrees])
max_airport = [airport['name'] for airport in out_degrees if airport['connections'] == max_degrees]

# 11. Z top10 wyświetl 10 pierwszych elementów:
top_10 = sorted(out_degrees, key=itemgetter('connections'), reverse=True)[:10]
for item in top_10:
    print(item)