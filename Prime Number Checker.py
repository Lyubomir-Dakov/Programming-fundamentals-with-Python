my_num = int(input())
my_num_is_prime = True

for i in range(2, my_num):
    if my_num % i == 0:
        my_num_is_prime = False
        break

if my_num_is_prime:
    print('True')
else:
    print('False')