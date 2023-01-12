key = ''.join(input().split())

next_line = input()


def find_type(my_string: str):
    new_string = my_string.split('&')
    my_type = new_string[1]
    return my_type


def find_coordinates(my_string: str):
    new_string_1 = my_string.split('<')
    new_string_2 = new_string_1[1].split('>')
    my_coordinates = new_string_2[0]
    return my_coordinates


while not next_line == 'find':
    resulted_string = ''

    if len(key) <= len(next_line):
        special_num = len(next_line) // len(key) + 1
        key *= special_num

    key = [int(x) for x in key]

    for num in range(len(next_line)):
        symbol = next_line[num]
        resulted_string += chr(ord(symbol) - key[num])

    treasure_type = find_type(resulted_string)
    coordinates = find_coordinates(resulted_string)
    print(f"Found {treasure_type} at {coordinates}")

    next_line = input()
