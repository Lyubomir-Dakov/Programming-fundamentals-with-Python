num_snowballs = int(input())
snowball_value_list = []
snowball_snow_list = []
snowball_time_list = []
snowball_quality_list = []

for _ in range(num_snowballs):
    snowball_snow = int(input())
    snowball_snow_list.append(snowball_snow)

    snowball_time = int(input())
    snowball_time_list.append(snowball_time)

    snowball_quality = int(input())
    snowball_quality_list.append(snowball_quality)

    snowball_value = (snowball_snow / snowball_time) ** snowball_quality
    snowball_value_list.append(snowball_value)

result_index = snowball_value_list.index(max(snowball_value_list))


print(f'{snowball_snow_list[result_index]} : {snowball_time_list[result_index]} = {int(snowball_value_list[result_index])} ({snowball_quality_list[result_index]})')
