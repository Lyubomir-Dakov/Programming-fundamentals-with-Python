line_1 = input().split(' ')


def switched_letters(word):
    my_word = [x for x in word]
    my_word[1], my_word[-1] = my_word[-1], my_word[1]
    return ''.join(my_word)


def code_to_chapter(word):
    left_part = []
    right_part = []
    for x in word:
        if x.isdigit():
            left_part.append(x)
        else:
            right_part.append(x)
    left_part = int(''.join(left_part))
    my_char = chr(left_part)
    my_word = my_char + ''.join(right_part)
    return my_word


result_list = []

for x in line_1:
    word_after_operation_1 = code_to_chapter(x)
    word_after_operation_2 = switched_letters(word_after_operation_1)
    result_list.append(word_after_operation_2)

print(' '.join(result_list))

