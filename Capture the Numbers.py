import re

regex = r"\d+"

new_line = input()
while True:
    if new_line:
        matches = re.findall(regex, new_line)
        for match in matches:
            if match:
                print(match, end=' ')
        new_line = input()
    else:
        break
