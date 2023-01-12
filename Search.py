n = int(input())
my_word = input()
full_list = []

for x in range(n):
    my_string = input()
    full_list.append(my_string)

filtered_list = [x for x in full_list if my_word in x]

print(full_list)
print(filtered_list)