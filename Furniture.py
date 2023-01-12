import re

purchase_info = input()
total_costs = 0
pattern = r">{2}(?P<furniture_name>[A-Za-z]+)<{2}(?P<price>\d+[\.\d+]*)!(?P<quantity>\d+)"
purchased_furniture = []

while not purchase_info == 'Purchase':
    furniture = re.finditer(pattern, purchase_info)
    for match in furniture:
        current_info = match.groupdict()
        furniture_name = current_info['furniture_name']
        price = float(current_info['price'])
        quantity = int(current_info['quantity'])

        purchased_furniture.append(furniture_name)
        total_costs += price * quantity

    purchase_info = input()

print("Bought furniture:")
for item in purchased_furniture:
    print(item)
print(f"Total money spend: {total_costs:.2f}")
