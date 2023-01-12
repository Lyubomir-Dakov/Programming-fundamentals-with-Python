my_string = input()

while not my_string == 'end':
    reverse_str = my_string[::-1]
    print(f"{my_string} = {reverse_str}")
    my_string = input()