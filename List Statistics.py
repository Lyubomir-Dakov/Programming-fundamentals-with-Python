n = int(input())
positive_list = []
negative_list = []

for i in range(n):
    new_int = int(input())
    if new_int >= 0:
        positive_list.append(new_int)
    else:
        negative_list.append(new_int)

print(positive_list)
print(negative_list)

print(f'Count of positives: {len(positive_list)}')
print(f'Sum of negatives: {sum(negative_list)}')
