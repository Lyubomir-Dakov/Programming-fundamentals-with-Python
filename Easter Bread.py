budget = float(input())
flour_price = float(input())

pack_of_eggs = flour_price * 0.75
l_milk = flour_price * 1.25
needed_milk = l_milk / 4

colored_eggs = 0
easter_bread = 0

one_bread_price = needed_milk + flour_price + pack_of_eggs

while True:
    budget -= one_bread_price
    if budget < 0:
        budget += one_bread_price
        break
    easter_bread += 1
    colored_eggs += 3

    if easter_bread % 3 == 0:
        colored_eggs -= (easter_bread - 2)


print(f"You made {easter_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")