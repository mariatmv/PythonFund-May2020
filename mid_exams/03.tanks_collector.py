owned_tanks = input().split(', ')
n = int(input())
for i in range(n):
    command = input().split(', ')
    todo = command[0]
    if todo == "Add":
        tank = command[1]
        if tank in owned_tanks:
            print("Tank is already bought")
        else:
            owned_tanks.append(tank)
            print("Tank successfully bought")
    elif todo == "Remove":
        tank = command[1]
        if tank in owned_tanks:
            owned_tanks.remove(tank)
            print("Tank successfully sold")
        else:
            print("Tank not found")
    elif todo == "Remove At":
        index = int(command[1])
        if 0 <= index <= len(owned_tanks):
            owned_tanks.pop(index)
            print("Tank successfully sold")
        else:
            print("Index out of range")
    else:
        index = int(command[1])
        tank = command[2]
        if 0 <= index <= len(owned_tanks):
            if tank not in owned_tanks:
                owned_tanks.insert(index, tank)
                print("Tank successfully bought")
            else:
                print("Tank is already bought")
        else:
            print("Index out of range")
print(', '.join(owned_tanks))