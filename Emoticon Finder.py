my_string = input()

for num in range(len(my_string)):
    if my_string[num] == ':':
        print(my_string[num] + my_string[num + 1])

