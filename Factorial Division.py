import math
num_1 = int(input())
num_2 = int(input())

res_1 = math.factorial(num_1)
res_2 = math.factorial(num_2)

last_result = res_1 / res_2
print(f'{last_result:.2f}')
