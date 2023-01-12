my_list = input().split('!')


def urgent(lst, item):
    if item in lst:
        pass
    else:
        lst.insert(0, item)
    return lst


def unnecessary(lst, item):
    if item in lst:
        lst.remove(item)
    else:
        pass
    return lst


def correct(lst, old_item, new_item):
    if old_item in lst:
        lst[lst.index(old_item)] = new_item
    else:
        pass
    return lst


def rearrange(lst, item):
    if item in lst:
        lst.remove(item)
        lst.append(item)
    else:
        pass
    return lst


while True:
    new_command = input()
    if new_command == "Go Shopping!":
        break

    my_command = new_command.split(' ')

    if 'Urgent' in my_command:
        grocery = my_command[1]
        urgent(my_list, grocery)

    elif 'Unnecessary' in my_command:
        grocery = my_command[1]
        unnecessary(my_list, grocery)

    elif 'Correct' in my_command:
        old_grocery = my_command[1]
        new_grocery = my_command[2]
        correct(my_list, old_grocery, new_grocery)

    elif 'Rearrange' in my_command:
        grocery = my_command[1]
        rearrange(my_list, grocery)

print(', '.join(my_list))