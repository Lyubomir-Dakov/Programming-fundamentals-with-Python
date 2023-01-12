line_1 = input().split(' ')
my_dict = {}

for x in range(0, len(line_1), 2):
    key = line_1[x]
    value = line_1[x+1]
    my_dict[key] = int(value)

print(my_dict)
