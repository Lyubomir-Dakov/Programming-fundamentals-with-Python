import re

demon_name = input()

health_pattern = r"(?<health>[^\d\+\-\*\/\.]+)"
damage_pattern = r"(?<damage>[\-*\d+(\.\d+)*\*+])"

demon_health = re.findall(health_pattern, demon_name)
print(type(demon_health))

# demon_damage = re.finditer(damage_pattern, demon_name)
# for match in demon_damage:
#     damage = match.group('damage')
#     print(damage)

