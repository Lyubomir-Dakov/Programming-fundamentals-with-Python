line_1 = input()
my_dict = {}


def check_if_user_in_lists_of_values(some_dict: dict, user: str):
    user_exists = False
    for the_list in some_dict.values():
        if user in the_list:
            user_exists = True
            break
    if user_exists:
        return True
    else:
        return False


def side_and_user(some_dict: dict, side: str, user: str):
    if side not in some_dict.keys() and not check_if_user_in_lists_of_values(some_dict, user):
        some_dict[side] = []
        some_dict[side].append(user)
    elif not check_if_user_in_lists_of_values(some_dict, user):
        some_dict[side].append(user)
    elif check_if_user_in_lists_of_values(some_dict, user):
        pass

    return some_dict


def user_to_side(some_dict: dict, side: str, user: str):
    if check_if_user_in_lists_of_values(some_dict, user):
        for k, v in some_dict.items():
            if user in v:
                v.remove(user)
        some_dict[side].append(user)

    elif not check_if_user_in_lists_of_values(some_dict, user):
        some_dict[side].append(user)

    elif not check_if_user_in_lists_of_values(some_dict, user) and side not in some_dict.keys():
        some_dict[side] = []
        some_dict[side].append(user)
    print(f"{user} joins the {side} side!")
    return some_dict


while not line_1 == "Lumpawaroo":
    if ' | ' in line_1:
        command = line_1.split(' | ')
        force_side = command[0]
        force_user = command[1]
        my_dict = side_and_user(my_dict, force_side, force_user)

    elif ' -> ' in line_1:
        command = line_1.split(' -> ')
        force_user = command[0]
        force_side = command[1]
        my_dict = user_to_side(my_dict, force_side, force_user)

    line_1 = input()

sorted_by_side = {k: v for k, v in sorted(my_dict.items(), key=lambda x: (len(x[1]), x[0]))}
for force_side, users in sorted_by_side.items():
    if len(users) > 0:
        print(f"Side: {force_side}, Members: {len(users)}")
        sorted_users = sorted(users)
        for name in sorted_users:
            print(f'! {name}')
