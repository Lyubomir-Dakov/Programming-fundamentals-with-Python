employees_happiness = [int(x) for x in input().split(' ')]
happiness_improvement_factor = int(input())

employees_happiness = [x * happiness_improvement_factor for x in employees_happiness]
average_happiness = sum(employees_happiness) / len(employees_happiness)

happy_employees = [x for x in employees_happiness if x >= average_happiness]

if len(happy_employees) >= len(employees_happiness) / 2:
    print(f"Score: {len(happy_employees)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employees_happiness)}. Employees are not happy!")

