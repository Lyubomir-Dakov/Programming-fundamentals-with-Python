new_line = input()

force_dict = {}


def add_user(my_dict: dict, side, user):
    for k, v in my_dict.items():
        if user in v:
            return my_dict

    if side not in my_dict:
        my_dict[side] = [user]
    else:
        my_dict[side].append(user)
    return my_dict


def change_user(my_dict: dict, side, user):
    for my_side, my_user in my_dict.items():
        if user in my_user:
            my_dict[my_side].remove(user)
            return add_user(my_dict, side, user)
    return add_user(my_dict, side, user)


while not new_line == "Lumpawaroo":

    if ' | ' in new_line:
        new_line = new_line.split(' | ')
        force_side, force_user = new_line
        force_dict = add_user(force_dict, force_side, force_user)
    elif ' -> ' in new_line:
        new_line = new_line.split(' -> ')
        force_user, force_side = new_line
        force_dict = change_user(force_dict, force_side, force_user)
        print(f"{force_user} joins the {force_side} side!")

    new_line = input()


sorted_dictionary = {k: v for k, v in sorted(force_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))}

for side, user in sorted_dictionary.items():
    if user:
        print(f"Side: {side}, Members: {len(user)}")
        for name in sorted(user):
            print(f'! {name}')

