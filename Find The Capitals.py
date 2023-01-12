my_string = input()
result_list = []

for x in range(len(my_string)):
    if ord(my_string[x]) in range(65, 91):
        result_list.append(x)

print(result_list)