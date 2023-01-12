divisor = int(input())
bound = int(input())

for result in range(bound, 0, -1):
    if result % divisor == 0:
        print(result)
        break



