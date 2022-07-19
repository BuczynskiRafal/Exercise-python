import json
from collections import namedtuple

user = namedtuple('User', ['id', 'first_name', 'last_name', 'email', 'gender', 'is_active'])


def json_to_object():
    with open('users.json', 'r') as file:
        users = json.load(file)
    users_collection = [user(*u.values()) for u in users]
    return users_collection


print(json_to_object())
