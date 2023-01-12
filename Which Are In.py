line_1 = input().split(', ')
line_2 = input().split(', ')

result_list = []

for x in line_1:
    for word in line_2:
        if x in word and x not in result_list:
            result_list.append(x)

print(result_list)
