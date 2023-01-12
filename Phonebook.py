new_line = input()
phone_book = {}

while not new_line.isdigit():
    name_number = new_line.split('-')
    phone_book[name_number[0]] = name_number[1]
    new_line = input()

for _ in range(int(new_line)):
    name = input()
    if name in phone_book:
        print(f"{name} -> {phone_book[name]}")
    else:
        print(f"Contact {name} does not exist.")
