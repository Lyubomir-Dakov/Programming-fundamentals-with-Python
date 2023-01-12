n = int(input())
my_list = []

for _ in range(n):
    my_integer = int(input())
    my_list.append(my_integer)


even_list = [x for x in my_list if x % 2 == 0]
odd_list = [x for x in my_list if x % 2 != 0]
positive_list = [x for x in my_list if x >= 0]
negative_list = [x for x in my_list if x < 0]

my_dict = {'even': even_list,
           'odd': odd_list,
           'negative': negative_list,
           'positive': positive_list}

new_command = input()
print(my_dict.get(new_command))