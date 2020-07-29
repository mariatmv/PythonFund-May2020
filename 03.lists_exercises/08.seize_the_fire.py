fires_with_cells = input().split("#")
water_given = int(input())
is_valid = False
effort = 0
total_fire = 0
print("Cells:")
for i in range(0, len(fires_with_cells)):
    current_fire = fires_with_cells[i].split(" = ")
    type_fire = current_fire[0]
    value = current_fire[1]
    if type_fire == "High":
        if 81 <= int(value) <= 125:
            is_valid = True
    elif type_fire == "Medium":
        if 51 <= int(value) <= 80:
            is_valid = True
    elif type_fire == "Low":
        if 1 <= int(value) <= 50:
            is_valid = True
    if is_valid:
        if water_given < int(value):
            continue
        print(f" - {value}")
        water_given -= int(value)
        current_effort = int(value) * 0.25
        effort += current_effort
        total_fire += int(value)
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")