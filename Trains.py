wagons = int(input())
train = [0] * wagons


def add_people(my_list, people):
    my_list[-1] += people
    return my_list


def insert_people(my_list, index, people):
    my_list[index] += people
    return my_list


def leave_people(my_list, index, people):
    my_list[index] -= people
    return my_list


command = input()
while command != 'End':
    new_command = command.split(' ')
    if new_command[0] == 'add':
        wagons = add_people(train, int(new_command[1]))
    elif new_command[0] == 'insert':
        wagons = insert_people(train, int(new_command[1]), int(new_command[2]))
    elif new_command[0] == 'leave':
        wagons = leave_people(train, int(new_command[1]), int(new_command[2]))
    command = input()

print(train)
