command = input()
my_dict = {}

while not command == 'statistics':
    new_command = command.split(': ')
    product = new_command[0]
    quantity = int(new_command[1])
    if product in my_dict:
        my_dict[product] += quantity
    else:
        my_dict[product] = quantity

    command = input()

print('Products in stock:')
for (product, quantity) in my_dict.items():
    print(f'- {product}: {quantity}')
print(f'Total Products: {len(my_dict)}')
print(f'Total Quantity: {sum(my_dict.values())}')

