line_1 = input().split(' ')
line_2 = [x for x in line_1 if len(x) % 2 == 0]

for word in line_2:
    print(word)
