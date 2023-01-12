n = int(input())
special_numbers = [5, 7, 11]

for num in range(1, n + 1):
    digits_list = [int(x) for x in str(num)]
    if not sum(digits_list) in special_numbers:
        print(f'{num} -> False')
    else:
        print(f'{num} -> True')
