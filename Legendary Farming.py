game = {'shards': 0,
        'fragments': 0,
        'motes': 0}

junk = {}

obtained_item = ''

while obtained_item == '':
    line_1 = input().split()
    for num in range(0, len(line_1), 2):
        material = line_1[num + 1].lower()
        quantity = int(line_1[num])
        if material in game:
            game[material] += quantity
            if game[material] >= 250:
                if material == 'shards':
                    obtained_item = 'Shadowmourne'
                    print(f"{obtained_item} obtained!")
                if material == 'fragments':
                    obtained_item = 'Valanyr'
                    print(f"{obtained_item} obtained!")
                if material == 'motes':
                    obtained_item = 'Dragonwrath'
                    print(f"{obtained_item} obtained!")
                game[material] -= 250
                break
        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += quantity

sorted_remaining_materials = {k: v for k, v in sorted(game.items(), key=lambda kvp: (-kvp[1], kvp[0]))}
for (key, value) in sorted_remaining_materials.items():
    print(f"{key}: {value}")

sorted_junk_items = {k: v for k, v in sorted(junk.items(), key=lambda item: item[0])}
for (key, value) in sorted_junk_items.items():
    print(f"{key}: {value}")
