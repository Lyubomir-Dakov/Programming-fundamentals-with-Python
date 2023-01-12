my_string = [int(x) for x in input().split('@')]
everybody_celebrates = True
cupid_current_position = 0
house_count = 0


def cupid_jump(string, position):
    if string[position] > 0:
        string[position] -= 2
        if my_string[position] == 0:
            print(f"Place {position} has Valentine's day.")
    else:
        print(f"Place {position} already had Valentine's day.")


while True:
    new_command = input().split(' ')

    if "Love!" in new_command:
        break

    jump_length = int(new_command[1])
    cupid_current_position += jump_length

    if cupid_current_position + 1 > len(my_string):
        cupid_current_position = 0
        cupid_jump(my_string, cupid_current_position)

    else:
        cupid_jump(my_string, cupid_current_position)

print(f"Cupid's last position was {cupid_current_position}.")

for x in my_string:
    if x != 0:
        everybody_celebrates = False
        house_count += 1

if everybody_celebrates:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {house_count} places.")




