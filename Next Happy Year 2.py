current_year = int(input())

while True:
    current_year += 1
    num_list = [int(x) for x in str(current_year)]
    if len(num_list) == len(list(set(num_list))):
        print(current_year)
        break

