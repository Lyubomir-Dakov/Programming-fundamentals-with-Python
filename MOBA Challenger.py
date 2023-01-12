line_1 = input()
player_dict = {}
total_skill = {}


def player_position_skill(my_dict: dict, my_player: str, my_position: str, my_skill: int):
    if my_player not in my_dict:
        my_dict[my_player] = {}
        my_dict[my_player][my_position] = my_skill
    else:
        if my_position not in my_dict[my_player]:
            my_dict[my_player][my_position] = my_skill
    if my_skill > my_dict[my_player][my_position]:
        my_dict[my_player][my_position] = my_skill
    return my_dict


def player_vs_player(my_dict: dict, name_1: str, name_2: str):
    if name_1 in my_dict and name_2 in my_dict:

        if len(my_dict[name_1]) >= len(my_dict[name_2]):
            for pos in my_dict[name_1]:
                if pos in my_dict[name_2]:
                    if my_dict[name_1][pos] > my_dict[name_2][pos]:
                        my_dict.pop(name_2)
                        break
                    elif my_dict[name_1][pos] < my_dict[name_2][pos]:
                        my_dict.pop(name_1)
                        break

        else:
            for pos in my_dict[name_2]:
                if pos in my_dict[name_1]:
                    if my_dict[name_1][pos] > my_dict[name_2][pos]:
                        my_dict.pop(name_2)
                    elif my_dict[name_1][pos] < my_dict[name_2][pos]:
                        my_dict.pop(name_1)

    return my_dict


while not line_1 == 'Season end':
    if ' -> ' in line_1:
        player_info = line_1.split(' -> ')
        player_name, position, skill = player_info[0], player_info[1], int(player_info[2])
        player_dict = player_position_skill(player_dict, player_name, position, skill)
    else:
        player_1, player_2 = line_1.split(' vs ')
        player_dict = player_vs_player(player_dict, player_1, player_2)

    line_1 = input()

for name, info in player_dict.items():
    if name not in total_skill:
        total_skill[name] = 0
    for pos, points in info.items():
        total_skill[name] += points

sorted_total_skill = {name: points for name, points in sorted(total_skill.items(), key=lambda kvp: (-kvp[1], kvp[0]))}

for name, total_skills in sorted_total_skill.items():
    print(f"{name}: {total_skills} skill")
    sorted_player_skill = {position: skill for position, skill in sorted(player_dict[name].items(), key=lambda kvp: (-kvp[1], kvp[0]))}
    for position, skill in sorted_player_skill.items():
        print(f"- {position} <::> {skill}")
