key = int(input())
n_lines = int(input())
result = ''

for _ in range(n_lines):
    new_letter = input()
    result += chr(key + ord(new_letter))

print(result)