def add_node(V, node):

    if node in V.keys():
        return
    else:
        V[node] = []


def add_edge(V, source, dest):

    if not source in V.keys() or not dest in V.keys():
        return
    else:
        if not dest in V[source]:
            V[source].append(dest)


metro = {
    "Staromestska": ["Mustek"],
    "Mustek": ["Staromestska", "Namesti Republiky", "Muzeum", "Narodni trida"],
    "Muzeum": ["Mustek", "Hlavni nadrazi"],
    "Narodni trida": ["Mustek"],
    "Namesti Republiky": ["Mustek", "Florenc"],
    "Florenc": ["Namesti Republiky", "Hlavni Nadrazi"],
    "Hlavni nadrazi": ["Florenc", "Muzeum"],
}

print(True if 'Staromestska' in  metro['Muzeum'] else False)
print(True if 'Hlavni Nadrazi' in metro['Florenc'] else False)
print("Muzeum is neighbour of Staromestska?", 'Muzeum' in metro['Staromestska'])
print('Hlavni Nadrazi is neighbour of Florenc', 'Hlavni Nadrazi' in metro['Florenc'])