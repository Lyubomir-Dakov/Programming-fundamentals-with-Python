line_1 = input()
my_dict = {}

for symbol in line_1:
    if symbol != ' ':
        if symbol not in my_dict:
            my_dict[symbol] = 0
        my_dict[symbol] += 1

for (key, value) in my_dict.items():
    print(f"{key} -> {value}")
