num_people = int(input())
capacity = int(input())

if num_people % capacity == 0:
    print(int(num_people / capacity))
else:
    result = int(num_people / capacity) + 1
    print(result)