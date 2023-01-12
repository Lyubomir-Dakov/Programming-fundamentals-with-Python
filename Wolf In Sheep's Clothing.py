my_string = input().split(', ')

if my_string[-1] == 'wolf':
    print("Please go away and stop eating my sheep")

else:
    n = 0
    for i in my_string[::-1]:
        if i == 'wolf':
            print(f"Oi! Sheep number {n}! You are about to be eaten by a wolf!")
            break
        n += 1
