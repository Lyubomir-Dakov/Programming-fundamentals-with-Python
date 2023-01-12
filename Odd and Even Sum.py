my_num = input()


def even_sum(num):
    even_digits = [int(num[x]) for x in range(len(num)) if int(num[x]) % 2 == 0]
    return sum(even_digits)


def odd_sum(num):
    odd_digits = [int(num[x]) for x in range(len(num)) if int(num[x]) % 2 != 0]
    return sum(odd_digits)


sum_of_even_digits = even_sum(my_num)
sum_of_odd_digits = odd_sum(my_num)
print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
