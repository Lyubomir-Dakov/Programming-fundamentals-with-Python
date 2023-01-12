line_1 = [int(x) for x in input().split(', ')]
result = [x for x in range(len(line_1)) if line_1[x] % 2 == 0]
print(result)
