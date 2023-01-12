num = int(input())

divisors = []

for x in range(1, num // 2 + 1):
    if num % x == 0:
        divisors.append(x)

if num == sum(divisors):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")