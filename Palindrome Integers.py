my_integers = input().split(', ')

for x in my_integers:
    if x[::] == x[::-1]:
        print('True')
    else:
        print('False')

