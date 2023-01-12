line_1 = [int(x) for x in input().split(', ')]
highest_group = 0

if max(line_1) % 10 == 0:
    highest_group = max(line_1) // 10
else:
    highest_group = max(line_1) // 10 + 1

for num in range(highest_group):
    sub_group = [x for x in line_1 if num * 10 < x <= (num + 1) * 10]
    print(f"Group of {(num + 1) * 10}'s: {sub_group}")

