v = {
    'P' : ['D1', 'D2', 'K', 'Q', 'H'],
    'D1': ['D2', 'P'],
    'D2': ['D1', 'P'],
    'K' : ['P', 'Q', 'H'],
    'Q' : ['P', 'K', 'H'],
    'H' : ['P', 'K', 'Q']
}


def node_degree(v, node):
    return len(v[node]) if node in v else False


# def graph_degree(v):
#     max_degree = 0
#     for node in v:
#         degree = node_degree(v, node)
#         if degree > max_degree:
#             max_degree = degree
#     return max_degree

def graph_degree(v):
    return max([node_degree(v, node) for node in v])

# print(node_degree(v, 'P'))
# print(node_degree(v, 'Q'))
# print(node_degree(v, 'D1'))
# print(node_degree(v, 'A'))

# print(graph_degree(v))

metro = {
    'Staromestska' : ['Mustek'],
    'Mustek' : ['Staromestska', 'Namesti Republiky', 'Muzeum', 'Narodni trida'],
    'Muzeum' : [ 'Mustek', 'Hlavni nadrazi'],
    'Narodni trida' : ['Mustek'],
    'Namesti Republiky' : ['Mustek', 'Florenc'],
    'Florenc': ['Namesti Republiky', 'Hlavni Nadrazi'],
    'Hlavni nadrazi' : ['Florenc', 'Muzeum']
}

print(graph_degree(metro))