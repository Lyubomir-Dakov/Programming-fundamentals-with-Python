first_string = input()
second_string = input()

for i in range(len(first_string)):
    if not first_string[i] == second_string[i]:
        left_part = second_string[: i + 1]
        right_part = first_string[i + 1:]
        result = left_part + right_part

        print(result)
    else:
        continue

