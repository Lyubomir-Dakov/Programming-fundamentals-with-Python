my_string = input().split()
alphabet = ['#', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
total_sum = 0

for small_str in my_string:
    left_letter = small_str[0]
    left_letter_position = alphabet.index(left_letter.lower())

    right_letter = small_str[-1]
    right_letter_position = alphabet.index(right_letter.lower())

    num = int(small_str[1: -1])

    if left_letter.isupper():
        num /= left_letter_position
    else:
        num *= left_letter_position

    if right_letter.isupper():
        num -= right_letter_position
    else:
        num += right_letter_position

    total_sum += num

print(f"{total_sum:.2f}")
