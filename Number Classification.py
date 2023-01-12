line_1 = [int(x) for x in input().split(', ')]
positive = [str(num) for num in line_1 if num >= 0]
negative = [str(num) for num in line_1 if num < 0]
even = [str(num) for num in line_1 if num % 2 == 0]
odd = [str(num) for num in line_1 if num % 2 != 0]

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")

