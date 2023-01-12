line_1 = [x for x in input()]
result = []

explosion = False
power = 0

for x in range(len(line_1)):

    if power == 0:
        explosion = False

    if explosion:
        if line_1[x] == '>':
            result.append(line_1[x])
            power += int(line_1[x + 1])
            continue
        power -= 1
        continue

    if line_1[x] == '>':
        explosion = True
        power = int(line_1[x + 1])
        result.append(line_1[x])

        continue

    result.append(line_1[x])

print(''.join(result))

