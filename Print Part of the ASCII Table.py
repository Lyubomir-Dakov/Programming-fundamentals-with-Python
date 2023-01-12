start_char = int(input())
end_char = int(input())

result = ''

for num in range(start_char, end_char + 1):
    result += chr(num)

result_2 = ' '.join([x for x in result])
print(result_2)