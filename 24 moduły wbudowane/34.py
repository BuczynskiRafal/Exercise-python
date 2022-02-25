import string


docs = 'programming in python'
alphabet = string.ascii_lowercase
code_map = dict(enumerate(alphabet))
code_map_inv = {val: key for key, val in code_map.items()}

print(code_map)
print(code_map_inv)

for letter in docs:
    if letter == ' ':
        continue
    else:
