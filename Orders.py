product = input()
quantity = int(input())

my_dict = {'coffee': 1.50,
           'water': 1.00,
           'coke': 1.40,
           'snacks': 2.00
           }


def calculate_price(product_price, the_quantity):
    total_price = product_price * the_quantity
    return total_price


result = calculate_price(my_dict.get(product), quantity)
print(f'{result:.2f}')
