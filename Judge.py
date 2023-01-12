line_1 = input()
my_dict = {}
individual_stats = {}

while not line_1 == 'no more time':
    info = line_1.split(' -> ')
    username, contest, points = info[0], info[1], int(info[2])
    if contest not in my_dict:
        my_dict[contest] = {}
        my_dict[contest][username] = points
    else:
        if username not in my_dict[contest]:
            my_dict[contest][username] = 0
        if points > my_dict[contest][username]:
            my_dict[contest][username] = points

    line_1 = input()

sorted_my_dict = {}

for contest, name_points in my_dict.items():
    sorted_name_points = {name: point for name, point in sorted(name_points.items(), key=lambda kvp: (-kvp[1], kvp[0]))}
    sorted_my_dict[contest] = sorted_name_points
    for name, point in name_points.items():
        if name not in individual_stats:
            individual_stats[name] = point
        else:
            individual_stats[name] += point

sorted_individual_stats = {name: point for name, point in sorted(individual_stats.items(), key=lambda kvp: (-kvp[1], kvp[0]))}

for contest, name_point in sorted_my_dict.items():
    print(f"{contest}: {len(name_point)} participants")
    count = 1
    for name, point in name_point.items():
        print(f"{count}. {name} <::> {point}")
        count += 1

print("Individual standings:")

count = 1
for name, point in sorted_individual_stats.items():
    print(f"{count}. {name} -> {point}")
    count += 1
