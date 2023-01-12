line_1 = input().split(', ')
winning_symbols = ['@', '#', '$', '^']


def split_my_ticket(my_ticket):
    my_left_part = my_ticket[:int(len(my_ticket) / 2)]
    my_right_part = my_ticket[int(len(my_ticket) / 2):]
    return my_left_part, my_right_part


def check_if_valid_ticket(my_ticket):
    if len(my_ticket) == 20:
        return True
    else:
        return False


def find_winning_symbols(my_string):
    count = 0
    str_win = ''
    win_parts = []
    for x in range(len(my_string)):
        symbol = my_string[x]
        if symbol not in winning_symbols:
            if count >= 6:
                win_parts.append(str_win)
            str_win = ''
            count = 0

        else:
            if symbol not in str_win:
                if count >= 6:
                    win_parts.append(str_win)
                count = 0
                str_win = ''
                count += 1
                str_win += symbol

            else:
                count += 1
                str_win += symbol

    if count >= 6:
        win_parts.append(str_win)

    return win_parts


for part in line_1:
    ticket = part.strip()

    if not check_if_valid_ticket(ticket):
        print("invalid ticket")
        continue

    left_part, right_part = split_my_ticket(ticket)

    left_win_symbols = ''.join(find_winning_symbols(left_part))
    right_win_symbols = ''.join(find_winning_symbols(right_part))

    uninterrupted_match_length = min([len(left_win_symbols), len(right_win_symbols)])

    if len(left_win_symbols) == 0 or len(right_win_symbols) == 0 or left_win_symbols[0] != right_win_symbols[0]:
        print(f"""ticket "{ticket}" - no match""")

    elif uninterrupted_match_length == 10:
        print(f"""ticket "{ticket}" - {uninterrupted_match_length}{left_win_symbols[0]} Jackpot!""")

    elif 6 <= uninterrupted_match_length <= 9:
        print(f"""ticket "{ticket}" - {uninterrupted_match_length}{left_win_symbols[0]}""")
