num_coffees = 0
lower_case_events = ['coding', 'dog', 'cat', 'movie']
upper_case_events = ['CODING', 'DOG', 'CAT', 'MOVIE']
need_extra_sleep = False

while True:
    new_command = input()

    if new_command == 'END':
        break

    if new_command in lower_case_events:
        num_coffees += 1

    elif new_command in upper_case_events:
        num_coffees += 2

    if num_coffees > 5:
        print('You need extra sleep')
        need_extra_sleep = True
        break

if not need_extra_sleep:
    print(num_coffees)
