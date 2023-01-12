my_num = float(input())

if my_num == 0:
    print('zero')

elif my_num < 0:
    if abs(my_num) < 1:
        print('small negative')
    elif abs(my_num) > 1000000:
        print('large negative')
    else:
        print('negative')

else:
    if abs(my_num) < 1:
        print('small positive')
    elif abs(my_num) > 1000000:
        print('large positive')
    else:
        print('positive')
