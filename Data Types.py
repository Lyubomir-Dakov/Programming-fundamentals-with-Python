data_type = input()
num = input()


def int_data_type(a):
    result = int(a) * 2
    print(result)


def real_data_type(a):
    result = float(a) * 1.5
    print(f'{result:.2f}')


def string_data_type(a):
    print(f'${a}$')


if data_type == 'int':
    int_data_type(num)
elif data_type == 'real':
    real_data_type(num)
elif data_type == 'string':
    string_data_type(num)

