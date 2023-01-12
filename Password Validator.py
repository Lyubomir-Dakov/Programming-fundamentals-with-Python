line_1 = input()


def length_of_pass(string):
    if not len(string) in range(6, 11):
        result = "Password must be between 6 and 10 characters"
        return result
    else:
        return True


def letter_digit(string):
    string_and_digit = True
    for x in string:
        if ord(x) in range(65, 123) or ord(x) in range(48, 58):
            pass
        else:
            result = "Password must consist only of letters and digits"
            return result
    if string_and_digit:
        return True


def at_least_2_digits(string):
    num_digits = 0
    for x in string:
        if ord(x) in range(48, 58):
            num_digits += 1
    if num_digits >= 2:
        return True
    else:
        result = "Password must have at least 2 digits"
        return result


def check_if_valid():
    if length_of_pass(line_1) == True and letter_digit(line_1) == True and at_least_2_digits(line_1) == True:
        print("Password is valid")
    else:
        result_1 = length_of_pass(line_1)
        result_2 = letter_digit(line_1)
        result_3 = at_least_2_digits(line_1)
        result_list = [result_1, result_2, result_3]
        for x in result_list:
            if x == True:
                pass
            else:
                print(x)


check_if_valid()
