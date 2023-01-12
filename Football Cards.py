cards = input().split(' ')
players_count_a = 11
players_count_b = 11
removed_players_a = []
removed_players_b = []
terminated_game = False

for x in cards:
    if 'A' in x and x[2:] not in removed_players_a:
        removed_players_a.append(x[2:])
        players_count_a -= 1
    elif 'B' in x and x[2:] not in removed_players_b:
        removed_players_b.append(x[2:])
        players_count_b -= 1

    if players_count_a < 7 or players_count_b < 7:
        terminated_game = True
        break

print(f"Team A - {players_count_a}; Team B - {players_count_b}")

if terminated_game:
    print("Game was terminated")

