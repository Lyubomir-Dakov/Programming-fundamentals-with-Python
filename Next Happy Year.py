current_year = int(input())

while True:
    happy_year = False
    current_year += 1
    happy_year_list = []
    for x in str(current_year):
        happy_year_list.append(x)
    if len(set(list(happy_year_list))) == len(happy_year_list):
        happy_year = True
        break

print(current_year)

