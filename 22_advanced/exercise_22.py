def hamming_distance(u, v):
    if len(u) != len(v):
        raise ValueError('Both vectors must be the same length.')
    distance = 0
    for i in range(len(u)):
        if u[i] != v[i]:
            distance += 1
    return distance


def hamming_weight_first(u):
    return hamming_distance(u, v=len(u)*'0')


def hamming_weight_second(u):
    return u.count('1')