prod_quantities = input().split(' ')
new_products = input().split(' ')
my_dict = {}

for x in range(0, len(prod_quantities), 2):
    product = prod_quantities[x]
    quantity = int(prod_quantities[x+1])
    my_dict[product] = quantity

for x in new_products:
    if x in my_dict.keys():
        print(f"We have {my_dict[x]} of {x} left")
    else:
        print(f"Sorry, we don't have {x}")

