import re

num = int(input())
star_enigma = {'Attacked planets': [], 'Destroyed planets': []}

for x in range(num):
    before_decrypt = input()
    pattern_1 = r"([star])"
    special_count = len(re.findall(pattern_1, before_decrypt.lower()))
    after_decrypt = ''.join([chr(ord(symbol) - special_count) for symbol in before_decrypt])

    pattern_2 = r"\@(?P<planet_name>[A-Za-z]+)([^\@\-\!\:\>])*\:+(?P<population>\d+)([^\@\-\!\:\>])*\!+(?P<attack_type>[AD])\!([^\@\-\!\:\>])*\-\>(?P<soldier_count>\d+)"
    info = re.finditer(pattern_2, after_decrypt)
    for match in info:
        planet_name = match.group('planet_name')
        population = match.group('population')
        attack_type = match.group('attack_type')
        soldier_count = match.group('soldier_count')
        if attack_type == 'A':
            star_enigma['Attacked planets'].append(planet_name)
        elif attack_type == 'D':
            star_enigma['Destroyed planets'].append(planet_name)

for key, list_of_planets in star_enigma.items():
    sorted_list_of_planets = [planet for planet in sorted(list_of_planets)]
    star_enigma[key] = sorted_list_of_planets

print(f"Attacked planets: {len(star_enigma['Attacked planets'])}")
for planet in star_enigma['Attacked planets']:
    print(f"-> {planet}")

print(f"Destroyed planets: {len(star_enigma['Destroyed planets'])}")
for planet in star_enigma['Destroyed planets']:
    print(f"-> {planet}")
