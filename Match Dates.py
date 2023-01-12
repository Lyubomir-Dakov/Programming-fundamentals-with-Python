import re

text = input()
regex = r"\b(\d{2})(.|-|-)([A-Z][a-z]{2})(\2)(\d{4}\b)"

for match in re.finditer(regex, text):
    day = match.group(1)
    month = match.group(3)
    year = match.group(5)
    print(f"Day: {day}, Month: {month}, Year: {year}")
