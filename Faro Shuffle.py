my_string = input().split(' ')
num_shuffles = int(input())


def shuffle(some_string):
    result_string = []
    left_part = some_string[:(len(some_string) // 2)]
    right_part = some_string[(len(some_string) // 2):]
    for x in range(len(left_part)):
        result_string.append(left_part[x])
        result_string.append(right_part[x])
    return result_string


for _ in range(num_shuffles):
    my_string = shuffle(my_string)

print(my_string)







