line_1 = input().upper()

number = ''
small_str = ''

result = ''
unique_symbols = []

for x in range(len(line_1)):
    symbol = line_1[x]

    if not symbol.isdigit():
        number = ''
        small_str += symbol
        if symbol not in unique_symbols:
            unique_symbols.append(symbol)

    else:
        number += symbol
        if x == len(line_1) - 1:
            result += small_str * int(number)
        elif not line_1[x + 1].isdigit():
            result += small_str * int(number)
            small_str = ''
            number = ''
        elif line_1[x + 1].isdigit():
            continue

print(f"Unique symbols used: {len(unique_symbols)}")
print(result)


