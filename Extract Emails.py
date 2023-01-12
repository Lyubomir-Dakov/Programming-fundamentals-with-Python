import re

text = input()

pattern = r"(^|(?<=\s))([a-z0-9]+[\.\-\_a-z0-9]*[a-z0-9]+)@[a-z]+(-[a-z]+)*\.[\.\-a-z]*\b"

result = re.finditer(pattern, text)

for match in result:
    print(match.group())

