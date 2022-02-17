V = ["mouse", "keyboard", "computer", "monitor", "printer"]
E = [{0, 2}, {1, 2}, {2, 3}, {2, 4}]


# def translate_to_matrix(V, E):
#     v_range = range(len(V))
#     matrix = [[1 if {v1, v2} in E else 0 for v2 in v_range] for v1 in v_range]
#     return matrix

# def translate_to_matrix(V, E):
#     v_range = range(len(V))
#     matrix = []
#     for v1 in v_range:
#         row = [1 if {v1, v2} in E else 0 for v2 in v_range]
#         matrix.append(row)
#     return matrix

def translate_to_matrix(V, E):
    v_range = range(len(V))
    matrix = []
    for v1 in v_range:
        row = []
        for v2 in v_range:
            if {v1, v2} in E:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix


matrix = translate_to_matrix(V, E)
for row in matrix:
    print(row)
