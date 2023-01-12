line_1 = [int(x) for x in input().split(', ')]
num_beggars = int(input())

beggar_income = []

for beggar in range(num_beggars):
    income = 0
    if beggar < len(line_1):
        for i in range(0, len(line_1), num_beggars):
            if beggar + i < len(line_1):
                income += line_1[beggar + i]
    beggar_income.append(income)

print(beggar_income)

