my_string = input()
my_list = [symbol for symbol in my_string]
result = [my_list[0]]

for symbol in my_list:
    if not symbol == result[-1]:
        result.append(symbol)

print(''.join(result))
