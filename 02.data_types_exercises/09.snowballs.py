snowballs_made = int(input())
highest_value = 0
max_snow = 0
max_time = 0
max_quantity = 0
for snowball in range(1, snowballs_made + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quantity = int(input())
    snowball_VALUE = (snowball_snow // snowball_time) ** snowball_quantity
    if snowball_VALUE > highest_value:
        highest_value = snowball_VALUE
        max_snow = snowball_snow
        max_time = snowball_time
        max_quantity = snowball_quantity
print(f"{max_snow} : {max_time} = {highest_value} ({max_quantity})")