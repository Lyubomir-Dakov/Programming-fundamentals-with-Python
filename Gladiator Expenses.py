lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
broken_shield = 0

for x in range(1, lost_fights_count + 1):
    if x % 2 == 0:
        expenses += helmet_price

    if x % 3 == 0:
        expenses += sword_price

    if x % 2 == 0 and x % 3 == 0:
        expenses += shield_price
        broken_shield += 1

    if broken_shield % 2 == 0 and broken_shield > 0:
        expenses += armor_price
        broken_shield = 0

print(f"Gladiator expenses: {expenses:.2f} aureus")

