line_1 = input().split()
str_1 = line_1[0]
str_2 = line_1[1]

special_num = min([len(word) for word in line_1])

total_sum = 0

for x in range(special_num):
    total_sum += ord(str_1[x]) * ord(str_2[x])

if len(str_1) != len(str_2):
    longer_str = ''.join([x for x in line_1 if len(x) > special_num])

    for symbol in longer_str[special_num:]:
        total_sum += ord(symbol)

print(total_sum)
