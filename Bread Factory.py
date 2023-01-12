day_events = input().split('|')
initial_energy = 100
initial_coins = 100
gained_energy = 0
events_completed = True


def rest_case(energy):
    global initial_energy, gained_energy
    if initial_energy + energy <= 100:
        initial_energy += energy
        gained_energy = energy
    else:
        gained_energy = 100 - initial_energy
        initial_energy += gained_energy
    print(f"You gained {gained_energy} energy.")
    print(f"Current energy: {initial_energy}.")


def order_case(coins):
    global initial_coins, initial_energy
    if initial_energy >= 30:
        initial_coins += coins
        initial_energy -= 30
        print(f"You earned {coins} coins.")
    else:
        initial_energy += 50
        print("You had to rest!")


def ingredient_case(ingredient, coins):
    global initial_coins, events_completed
    if initial_coins >= coins:
        initial_coins -= coins
        print(f"You bought {ingredient}.")
    else:
        events_completed = False
        print(f"Closed! Cannot afford {ingredient}.")


for x in day_events:
    small_list = x.split('-')
    if 'rest' in small_list:
        rest_case(int(small_list[1]))
    elif 'order' in small_list:
        order_case(int(small_list[1]))
    else:
        ingredient_case(small_list[0], int(small_list[1]))
        if not events_completed:
            break


if events_completed:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")

