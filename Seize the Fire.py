fire_and_cells = input().split('#')
water = int(input())
effort = 0
total_fire = 0
result_list = ['Cells:']


def check_if_valid(fire_type, value):
    fire_level = {'Low': range(1, 51),
                  'Medium': range(51, 81),
                  'High': range(81, 126)}
    if int(value) in fire_level.get(fire_type):
        return True
    else:
        return False


for x in fire_and_cells:
    step_through_fire = x.split(' = ')
    if check_if_valid(step_through_fire[0], step_through_fire[1]) and water >= int(step_through_fire[1]):
        water -= int(step_through_fire[1])
        effort += int(step_through_fire[1]) * 0.25
        total_fire += int(step_through_fire[1])
        result_list.append(f'- {step_through_fire[1]}')

for x in result_list:
    print(x)

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")


