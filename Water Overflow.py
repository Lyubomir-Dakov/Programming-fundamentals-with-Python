lines = int(input())
tank = 0

for x in range(lines):
    pour_water = int(input())

    if pour_water + tank > 255:
        print("Insufficient capacity!")

    else:
        tank += pour_water

print(tank)
