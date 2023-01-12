import math

x_1 = int(input())
y_1 = int(input())
x_2 = int(input())
y_2 = int(input())

distance_1 = math.sqrt(x_1 ** 2 + y_1 ** 2)
distance_2 = math.sqrt(x_2 ** 2 + y_2 ** 2)

if distance_1 < distance_2:
    print(f'({x_1}, {y_1})')
elif distance_1 > distance_2:
    print(f'({x_2}, {y_2})')
else:
    print(f'({int(x_1)}, {int(y_1)})')
