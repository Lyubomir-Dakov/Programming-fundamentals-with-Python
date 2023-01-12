import re

racer_names = input().split(', ')
new_line = input()
racing_info = {}
letters_regex = r"[A-Za-z]+"
numbers_regex = r"[0-9]"
place = {1: '1st', 2: '2nd', 3: '3rd'}
count = 1

while not new_line == 'end of race':
    name = ''.join(re.findall(letters_regex, new_line))
    distance = sum([int(num) for num in re.findall(numbers_regex, new_line)])
    if name in racer_names:
        if name not in racing_info:
            racing_info[name] = 0
        racing_info[name] += distance

    new_line = input()

sorted_racing_info = {name: distance for name, distance in sorted(racing_info.items(), key=lambda kvp: -kvp[1])}
for name in sorted_racing_info.keys():
    if count <= 3:
        print(f'{place[count]} place: {name}')
        count += 1
    else:
        break

