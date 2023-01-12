num_1 = int(input())
num_2 = int(input())
num_3 = int(input())


def sum_numbers(a, b):
    return a + b


def subtract(a, b):
    return a - b


num_4 = sum_numbers(num_1, num_2)

result = subtract(num_4, num_3)
print(result)