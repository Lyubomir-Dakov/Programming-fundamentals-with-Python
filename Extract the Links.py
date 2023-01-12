import re

new_line = input()

regex = r"(?P<sub_domain>w{3})\.(?P<domain_name>[A-Za-z\d\-]+)(?P<domain_extension>(\.[a-z]+)+)"

while True:
    if new_line:
        result = re.finditer(regex, new_line)
        for match in result:
            print(match.group())
    else:
        break

    new_line = input()
