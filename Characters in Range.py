char_1 = input()
char_2 = input()

result = ' '.join([chr(x) for x in range(ord(char_1) + 1, ord(char_2))])
print(result)
