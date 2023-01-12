my_string = input().split(', ')
without_zero = [int(x) for x in my_string if not x == '0']
num_zeroes = len(my_string) - len(without_zero)

for _ in range(num_zeroes):
    without_zero.append(0)

print(without_zero)