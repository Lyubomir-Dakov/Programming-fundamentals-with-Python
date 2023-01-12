line_1 = input()
courses = {}

while not line_1 == 'end':
    course_info = line_1.split(' : ')
    course_name = course_info[0]
    student_name = course_info[1]
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)

    line_1 = input()

courses = sorted(courses.items(), key=lambda x: -len(x[1]))

for (course, students) in courses:
    students = sorted(students)
    print(f"{course}: {len(students)}")
    for stud in students:
        print(f"-- {stud}")

