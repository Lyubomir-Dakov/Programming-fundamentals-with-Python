line_1 = input()
my_dict = {}

while not line_1 == 'buy':
    product_info = line_1.split()
    product_name = product_info[0]
    price = float(product_info[1])
    quantity = int(product_info[2])

    if product_name not in my_dict:
        my_dict[product_name] = [0.00, 0]
    my_dict[product_name][0] = price
    my_dict[product_name][1] += quantity

    line_1 = input()

for (product, info) in my_dict.items():
    total_price = info[0] * info[1]
    print(f"{product} -> {total_price:.2f}")
