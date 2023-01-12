line_1 = input().split(', ')


def collect_item(my_list, new_item):
    if new_item not in my_list:
        my_list.append(new_item)
    return my_list


def drop_item(my_list, new_item):
    if new_item in my_list:
        my_list.remove(new_item)
    return my_list


def combine_items(my_list, old_item, new_item):
    if old_item in my_list:
        my_list.insert(my_list.index(old_item) + 1, new_item)
    return my_list


def renew_item(my_list, new_item):
    if new_item in my_list:
        my_list.remove(new_item)
        my_list.append(new_item)
    return my_list


command = input()

while not command == 'Craft!':

    new_command = command.split(' - ')

    if new_command[0] == 'Collect':
        collect_item(line_1, new_command[1])
    elif new_command[0] == 'Drop':
        drop_item(line_1, new_command[1])
    elif new_command[0] == 'Combine Items':
        old_and_new_item = [word for word in (new_command[1]).split(':')]
        combine_items(line_1, old_and_new_item[0], old_and_new_item[1])
    elif new_command[0] == 'Renew':
        renew_item(line_1, new_command[1])

    command = input()

print(', '.join(line_1))
