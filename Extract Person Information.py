lines = int(input())


def find_name(my_string):
    search_name_1 = my_string.split('@')
    search_name_2 = search_name_1[1].split('|')
    my_name = search_name_2[0]
    return my_name


def find_age(my_string):
    search_name_1 = my_string.split('#')
    search_name_2 = search_name_1[1].split('*')
    my_age = search_name_2[0]
    return my_age


for _ in range(lines):
    next_line = input()
    name = find_name(next_line)
    age = find_age(next_line)
    print(f"{name} is {age} years old.")
