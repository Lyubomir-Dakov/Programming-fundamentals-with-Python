to_do_notes = input()
result_list = [0] * 11

while not to_do_notes == 'End':
    command = to_do_notes.split('-')
    result_list[int(command[0])] = command[1]
    to_do_notes = input()

result_list = [x for x in result_list if not x == 0]
print(result_list)

