collection = input().split('|')
budget = int(input())
new_prices = []
profit = 0


def check_if_valid(item_type, item_price):
    my_dict = {'Clothes': 50,
               'Shoes': 35,
               'Accessories': 20.5}
    if item_price <= my_dict.get(item_type):
        return True
    else:
        return False


for x in collection:
    type_and_price = x.split('->')
    if check_if_valid(type_and_price[0], float(type_and_price[1])) and budget >= float(type_and_price[1]):
        budget -= float(type_and_price[1])
        new_prices.append(float(type_and_price[1]) * 1.4)
        profit += float(type_and_price[1]) * 0.4


for x in new_prices:
    print(f'{float(x):.2f}', end=' ')

print()
print(f'Profit: {profit:.2f}')

if budget + sum(new_prices) >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")

