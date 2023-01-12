companions_count = int(input())
days = int(input())
coins = 0

for x in range(1, days +1):
    if x % 10 == 0:
        companions_count -= 2

    if x % 15 == 0:
        companions_count += 5

    coins += 50 - 2 * companions_count

    if x % 3 == 0:
        coins -= 3 * companions_count

    if x % 5 == 0:
        coins += 20 * companions_count
        if x % 3 == 0:
            coins -= 2 * companions_count

print(f"{companions_count} companions received {coins // companions_count} coins each.")

