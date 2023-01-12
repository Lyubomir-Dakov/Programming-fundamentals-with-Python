num = int(input())

result_1 = str(num) + '%'
result_2 = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']

for x in range(num // 10):
    result_2[x] = '%'

result_2 = ''.join(result_2)
if result_2 == '%' * 10:
    print('100% Complete!')
    print(f'[{result_2}]')
else:
    print(f'{result_1} [{result_2}]')
    print('Still loading...')
