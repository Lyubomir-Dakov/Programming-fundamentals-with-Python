line_1 = [int(x) for x in input().split('@')]
cupid_current_position = 0
mission_successful = True
count_not_celebrating_houses = 0

command = input()

while not command == 'Love!':

    new_command = command.split(' ')
    jump = int(new_command[1])

    if cupid_current_position + jump >= len(line_1):
        cupid_current_position = 0
    else:
        cupid_current_position += jump

    if line_1[cupid_current_position] == 0:
        print(f"Place {cupid_current_position} already had Valentine's day.")
    else:
        line_1[cupid_current_position] -= 2
        if line_1[cupid_current_position] == 0:
            print(f"Place {cupid_current_position} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {cupid_current_position}.")

for num in line_1:
    if not num == 0:
        mission_successful = False
        count_not_celebrating_houses += 1

if mission_successful:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {count_not_celebrating_houses} places.")

