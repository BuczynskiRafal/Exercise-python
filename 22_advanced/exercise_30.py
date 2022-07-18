import json


def json_to_csv():
    with open('users.json', 'r') as file:
        data = json.load(file)
    header = ','.join(data[0])
    users = [user.values() for user in data]
    rows = [','.join(str(item) for item in user) for user in users]
    with open('users.csv', 'w') as file:
        file.write(header + '\n')
        for row in rows:
            file.write(row + '\n')

print(json_to_csv())