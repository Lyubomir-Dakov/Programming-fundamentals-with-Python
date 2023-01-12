my_list = [int(x) for x in input().split(' ')]
count_to_remove = int(input())

for _ in range(count_to_remove):
    need_to_pop = min(my_list)
    my_list.pop(my_list.index(need_to_pop))

my_list = [str(x) for x in my_list]
print(', '.join(my_list))
