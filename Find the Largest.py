numbers = input()
list_of_digits = sorted([x for x in numbers])
result_list = (list_of_digits[::-1])
result = ''.join(result_list)

print(result)