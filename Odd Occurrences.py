line_1 = [word.lower() for word in input().split(' ')]
my_dict = {}

for word in line_1:
    if word not in my_dict:
        my_dict[word] = 0
    my_dict[word] += 1

result = []

for (key, value) in my_dict.items():
    if not value % 2 == 0:
        if key not in result:
            result.append(key)

print(' '.join(result))
