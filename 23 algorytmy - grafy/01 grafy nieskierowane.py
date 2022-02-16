V = ['Princess', 'Dwarfs', 'Queen', 'King', 'Hunter']
E = [
    [0, 1],
    [0, 2],
    [0, 3],
    [0, 4],
    [2, 3],
    [2, 4],
    [3, 4]
]


# Who knows king?
# def who_knows_person(person: str, E: list, V:list) -> list:
#     index = V.index(person)
#     friends = []
#     for p in E:
#         if index in p:
#             for num in p:
#                 if num != index:
#                     friends.append(V[num])
#     return(friends)


# Who knows king?
def who_knows_person(person: str, E: list, V:list) -> list:
    friends = []
    for p1, p2 in E:
        if V[p1] == person:
            friends.append(V[p2])
        else:
            if V[p2] == person:
                friends.append(V[p1])
    return(friends)

print(who_knows_person('King', E, V))