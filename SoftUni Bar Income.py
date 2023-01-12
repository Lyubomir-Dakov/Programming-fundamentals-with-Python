import re

order_info = input()
regex = r'\%(?P<customer>[A-Z][a-z]+)\%[^\|\$\%\.]*?\<(?P<product>\w+)\>[^\|\$\%\.]*?\|(?P<count>[\d+]+)\|[\w\-]*?(?P<price>[\d.]+[\d+])\$$'
total_income = 0

while not order_info == 'end of shift':
    info = re.finditer(regex, order_info)
    for match in info:
        customer = match.group('customer')
        product = match.group('product')
        count = int(match.group('count'))
        price = float(match.group('price'))

        total_price = count * price
        total_income += total_price
        print(f"{customer}: {product} - {total_price:.2f}")

    order_info = input()

print(f"Total income: {total_income:.2f}")
