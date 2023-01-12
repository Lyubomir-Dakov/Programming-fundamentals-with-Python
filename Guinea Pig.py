food_per_month = float(input())
hay_per_month = float(input())
cover_per_month = float(input())
pig_weight = float(input())
everything_is_enough = True

for x in range(1, 31):
    food_per_month -= 0.3

    if x % 2 == 0:
        hay_per_month -= food_per_month * 0.05

    if x % 3 == 0:
        cover_per_month -= pig_weight / 3

    if food_per_month <= 0 or hay_per_month <= 0 or cover_per_month <= 0:
        print("Merry must go to the pet store!")
        everything_is_enough = False
        break

if everything_is_enough:
    print(f"Everything is fine! Puppy is happy! Food: {food_per_month:.2f}, Hay: {hay_per_month:.2f}, Cover: {cover_per_month:.2f}.")
