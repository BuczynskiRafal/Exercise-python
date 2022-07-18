import json


def filter_active_users():
    with open('users.json', 'r') as file:
        users = json.load(file)
        active_users = [user for user in users if user['is_active']]
    with open('active_users.json', 'w') as file:
        json.dump(active_users, file, indent=2)


print(filter_active_users())
