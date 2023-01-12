contests_and_passwords = input()
dict_contest_pass = {}
dict_user_points = {}

while not contests_and_passwords == 'end of contests':
    contest, password = contests_and_passwords.split(':')
    dict_contest_pass[contest] = password
    contests_and_passwords = input()

username_and_points = input()

while not username_and_points == 'end of submissions':
    contest, password, username, points = username_and_points.split('=>')
    if contest in dict_contest_pass and password == dict_contest_pass[contest]:
        if username not in dict_user_points:
            dict_user_points[username] = {}
            dict_user_points[username][contest] = int(points)
        else:
            if contest not in dict_user_points[username]:
                dict_user_points[username][contest] = int(points)
            else:
                if dict_user_points[username][contest] < int(points):
                    dict_user_points[username][contest] = int(points)

    username_and_points = input()

points_dict = {}

for stud, results in dict_user_points.items():
    total_points_of_user = 0
    for c, p in dict_user_points[stud].items():
        total_points_of_user += p
    points_dict[stud] = total_points_of_user

for stud, point in points_dict.items():
    if point == max(points_dict.values()):
        print(f"Best candidate is {stud} with total {point} points.")

print('Ranking:')

my_sorted_dict = {k: v for k, v in sorted(dict_user_points.items(), key=lambda kvp: kvp[0])}

for stud, info in my_sorted_dict.items():
    print(f'{stud}')
    my_sorted_info = {k: v for k, v in sorted(info.items(), key=lambda kvp: -kvp[1])}
    for contest, points in my_sorted_info.items():
        print(f'#  {contest} -> {points}')
