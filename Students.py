basic_info = input()
my_dict = {}

while ':' in basic_info:
    information = basic_info.split(':')
    name = information[0]
    student_id = int(information[1])
    course = information[2]
    if course not in my_dict:
        my_dict[course] = {}
        my_dict[course][name] = student_id
    my_dict[course][name] = student_id

    basic_info = input()

searched_course = ' '.join(basic_info.split('_'))
searched_info = my_dict[searched_course]

for (key, value) in searched_info.items():
    print(f"{key} - {value}")
