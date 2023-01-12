gifts = input().split(' ')


def out_of_stock(gift, collection):
    for x in range(len(collection)):
        if collection[x] == gift:
            collection[x] = 'None'
    return collection


def required(gift, index, collection):
    if int(index) < len(collection):
        collection[int(index)] = gift
    return collection


def just_in_case(gift, collection):
    collection[-1] = gift
    return collection


while True:
    new_command = input()

    if new_command == "No Money":
        break

    my_command = new_command.split(' ')
    if 'OutOfStock' in my_command:
        gifts = out_of_stock(my_command[1], gifts)

    elif 'Required' in my_command:
        gifts = required(my_command[1], my_command[2], gifts)

    elif 'JustInCase' in my_command:
        gifts = just_in_case(my_command[1], gifts)

gifts = ' '.join([x for x in gifts if x != 'None'])
print(gifts)
