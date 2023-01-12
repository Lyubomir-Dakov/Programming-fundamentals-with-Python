quantity = int(input())
days = int(input())

christmas_spirit = 0
total_cost = 0

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

for x in range(1, days + 1):

    if x % 11 == 0:
        quantity += 2

    if x % 2 == 0:
        total_cost += ornament_set * quantity
        christmas_spirit += 5

    if x % 3 == 0:
        total_cost += (tree_skirt + tree_garlands) * quantity
        christmas_spirit += 13
        if x % 5 == 0:
            christmas_spirit += 30

    if x % 5 == 0:
        total_cost += tree_lights * quantity
        christmas_spirit += 17

    if x % 10 == 0:
        christmas_spirit -= 20
        total_cost += tree_skirt + tree_garlands + tree_lights


if days % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {christmas_spirit}")
