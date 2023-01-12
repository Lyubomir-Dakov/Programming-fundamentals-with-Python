my_nums = input().split(' ')


def even_numbers(string):
    even_nums = [int(x) for x in string if int(x) % 2 == 0]
    return even_nums


print(even_numbers(my_nums))