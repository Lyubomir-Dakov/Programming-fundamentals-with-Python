number_of_electrons = int(input())

shells = []
n = 1

while not number_of_electrons == 0:
    new_num = 2 * n ** 2
    if new_num <= number_of_electrons:
        shells.append(new_num)
        number_of_electrons -= new_num
    else:
        shells.append(number_of_electrons)
        number_of_electrons = 0
    n += 1

print(shells)
