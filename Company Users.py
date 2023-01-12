line_1 = input()
my_dict = {}

while not line_1 == 'End':
    info = line_1.split(' -> ')
    company_name = info[0]
    employees_id = info[1]

    if company_name not in my_dict:
        my_dict[company_name] = []
    if employees_id not in my_dict[company_name]:
        my_dict[company_name].append(employees_id)

    line_1 = input()

my_sorted_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda x: x[0])}

for company in my_sorted_dict:
    print(f'{company}')
    for emp_id in my_sorted_dict[company]:
        print(f'-- {emp_id}')
