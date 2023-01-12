n = int(input())
result = 0

for _ in range(n):
    new_char = input()
    result += ord(new_char)

print(f'The sum equals: {result}')