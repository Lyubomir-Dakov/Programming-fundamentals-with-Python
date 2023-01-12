line_1 = input().split(', ')
my_dict = {}

for symbol in line_1:
    my_dict[symbol] = ord(symbol)

print(my_dict)