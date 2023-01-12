import re

text = input()

regex = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'

result = re.finditer(regex, text)

for match in result:
    print(match.group(0), end=' ')
