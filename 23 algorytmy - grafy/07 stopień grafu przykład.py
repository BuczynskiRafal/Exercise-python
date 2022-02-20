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

print(f'Processed {line_count} lines.')


out_degrees = []
for origin, destinations in network.items():
    out_degrees.append({ 'name': origin, 'connections' : len(destinations) })

max_airport =