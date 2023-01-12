room_number = int(input())
total_free_chairs = 0
everybody_can_sit = True


for room_num in range(1, room_number + 1):
    new_command = input().split(' ')
    num_chairs = len(new_command[0])
    num_visitors = int(new_command[1])
    if num_chairs < num_visitors:
        needed_chairs_in_room = num_visitors - num_chairs
        print(f"{needed_chairs_in_room} more chairs needed in room {room_num}")
        everybody_can_sit = False
    else:
        total_free_chairs += num_chairs - num_visitors

if everybody_can_sit:
    print(f"Game On, {total_free_chairs} free chairs left")
