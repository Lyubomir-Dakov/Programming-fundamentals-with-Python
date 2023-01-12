info = input()
dict_students = {}
language_dict = {}

while not info == 'exam finished':
    next_line = info.split('-')
    if len(next_line) == 3:
        username, language, points = next_line
        if username not in dict_students:
            dict_students[username] = []
        dict_students[username].append(int(points))
        if language not in language_dict:
            language_dict[language] = 0
        language_dict[language] += 1
    else:
        banned_user = next_line[0]
        dict_students.pop(banned_user)

    info = input()

sorted_students_dict = {k: max(v) for k, v in sorted(dict_students.items(), key=lambda kvp: (-max(kvp[1]), kvp[0]))}
print("Results:")
for student, points in sorted_students_dict.items():
    print(f'{student} | {points}')

sorted_language_dict = {k: v for k, v in sorted(language_dict.items(), key=lambda kvp: (-kvp[1], kvp[0]))}
print("Submissions:")
for language, count in sorted_language_dict.items():
    print(f'{language} - {count}')
