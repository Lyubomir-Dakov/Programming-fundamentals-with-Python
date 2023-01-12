num_rows = int(input())
my_dict = {}

for _ in range(num_rows):
    name_of_student = input()
    grade_of_student = float(input())

    if name_of_student not in my_dict:
        my_dict[name_of_student] = []
    my_dict[name_of_student].append(grade_of_student)

my_dict = {k: sum(v)/len(v) for k, v in my_dict.items() if sum(v)/len(v) >= 4.5}
my_dict = dict(sorted(my_dict.items(), key=lambda x: -x[1]))

for (k, v) in my_dict.items():
    print(f"{k} -> {v:.2f}")
