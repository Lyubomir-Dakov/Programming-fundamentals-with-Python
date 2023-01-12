import re

text = input().lower()
word = input()

pattern = fr"\b{word.lower()}\b"

result = re.findall(pattern, text)
print(len(result))
