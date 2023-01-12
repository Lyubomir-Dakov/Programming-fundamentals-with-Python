chr_1 = input()
chr_2 = input()

my_string = input()

total_sum = 0

for symbol in my_string:
    if ord(symbol) in range(ord(chr_1) + 1, ord(chr_2)):
        total_sum += ord(symbol)

print(total_sum)
