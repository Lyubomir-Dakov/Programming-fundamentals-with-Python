str_1 = input()
str_2 = ''

for symbol in str_1:
    str_2 += chr(ord(symbol) + 3)

print(str_2)
