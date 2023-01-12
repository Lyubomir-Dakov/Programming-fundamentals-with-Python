message = input()


def move(my_string, num):
    left_part = my_string[:num]
    my_string = my_string[num:] + left_part
    return my_string


def insert(my_string, my_index, my_value):
    left_part = my_string[:my_index]
    right_part = my_string[my_index:]
    my_string = left_part + my_value + right_part
    return my_string


def change_all(my_string: str, my_sub_str, my_replace_str):
    my_string = my_string.replace(my_sub_str, my_replace_str)
    return my_string


new_line = input()
while not new_line == 'Decode':
    command = new_line.split('|')
    if command[0] == 'ChangeAll':
        message = change_all(message, command[1], command[2])
    elif command[0] == 'Insert':
        message = insert(message, int(command[1]), command[2])
    elif command[0] == 'Move':
        message = move(message, int(command[1]))

    new_line = input()

print(f"The decrypted message is: {message}")
