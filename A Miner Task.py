new_line = input()
my_list = []
my_dict = {}

while not new_line == 'stop':
    my_list.append(new_line)
    new_line = input()

my_list = [int(my_list[num]) if num % 2 != 0 else my_list[num] for num in range(len(my_list))]

for x in range(0, len(my_list), 2):
    resource = my_list[x]
    if resource not in my_dict:
        my_dict[resource] = 0
    my_dict[resource] += my_list[x + 1]

for (resources, quantities) in my_dict.items():
    print(f"{resources} -> {quantities}")
