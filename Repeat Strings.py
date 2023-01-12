strings = input().split()
result = ''

for word in strings:
    n = len(word)
    result += word * n

print(result)
