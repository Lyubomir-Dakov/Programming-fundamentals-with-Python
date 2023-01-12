my_string = input().lower()
my_list = ["sand", "water", "fish", "sun"]
result = 0
current_string = ''


def check_word(string, my_word):
    global result
    global current_string
    if my_word in string:
        result += 1
        current_string = ''


for i in my_string:
    current_string += i
    for x in my_list:
        check_word(current_string, x)

print(result)

