first_can_handle = int(input())
second_can_handle = int(input())
third_can_handle = int(input())
people = int(input())
all_handle_per_hour = first_can_handle + second_can_handle + third_can_handle
needed_time = 0
while people > 0:
    people -= all_handle_per_hour
    needed_time += 1
    if needed_time % 4 == 0 and needed_time != 0:
        needed_time += 1
print(f"Time needed: {needed_time}h.")