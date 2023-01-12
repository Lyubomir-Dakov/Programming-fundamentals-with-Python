country_names = input().split(', ')
capital_cities = input().split(', ')
my_dict = dict(zip(country_names, capital_cities))

for (country, capital_city) in my_dict.items():
    print(f"{country} -> {capital_city}")
