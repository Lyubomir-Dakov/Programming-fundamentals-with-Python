dwarfs = {}

data = input()
while not data == 'Once upon a time':
    dwarf_data = data.split(' <:> ')
    name, hat_color, physic = dwarf_data[0], dwarf_data[1], int(dwarf_data[2])
    if name not in dwarfs.values():
        dwarfs[hat_color] = {'dwarf_name': name, 'dwarf_physics': physic}


    data = input()

print(dwarfs)