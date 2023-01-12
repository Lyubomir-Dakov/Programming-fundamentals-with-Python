import re

text = input()
regex = r"(\+359 2 \d{3} \d{4})|(\+359-2-\d{3}-\d{4})\b"

result = re.finditer(regex, text)
result_2 = []

for match in result:
    result_2.append(match.group())

print(', '.join(result_2))
