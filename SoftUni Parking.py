num_commands = int(input())
my_dictionary = {}


def register_username(database: dict, username: str, license_plate_number: str):
    if username in database:
        print(f"ERROR: already registered with plate number {database[username]}")
    else:
        database[username] = license_plate_number
        print(f"{username} registered {license_plate_number} successfully")


def unregister_username(database: dict, username: str):
    if username not in database:
        print(f"ERROR: user {username} not found")
    else:
        database.pop(username)
        print(f"{username} unregistered successfully")


for _ in range(num_commands):
    command = input().split()
    if command[0] == 'register':
        user_name = command[1]
        license_number = command[2]
        register_username(my_dictionary, user_name, license_number)

    elif command[0] == 'unregister':
        user_name = command[1]
        unregister_username(my_dictionary, user_name)

for (key, value) in my_dictionary.items():
    print(f"{key} => {value}")
