from _collections import OrderedDict
n = int(input())
cars = {}
for i in range(1, n + 1):
    data = input().split('|')
    name = data[0]
    mileage = int(data[1])
    fuel = int(data[2])
    cars[name] = [mileage, fuel]
command = input()
while command != "Stop":
    command = command.split(' : ')
    todo = command[0]
    if todo == "Drive":
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        if cars[car][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car][0] += distance
            cars[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car][0] >= 100000:
            print(f"Time to sell the {car}!")
            del cars[car]
    elif todo == "Refuel":
        car = command[1]
        fuel = int(command[2])
        if cars[car][1] + fuel > 75:
            diff = (cars[car][1] + fuel) - 75
            newdiff = fuel - diff
            cars[car][1] += newdiff
            print(f"{car} refueled with {newdiff} liters")
        else:
            cars[car][1] += fuel
            print(f"{car} refueled with {fuel} liters")
    else:
        car = command[1]
        km = int(command[2])
        if cars[car][0] - km <= 10000:
            cars[car][0] = 10000
        else:
            cars[car][0] -= km
            print(f"{car} mileage decreased by {km} kilometers")
    command = input()
sorted_cars = OrderedDict(sorted(cars.items(), key=lambda x: x[1], reverse=True))
for k, v in sorted_cars.items():
    print(f"{k} -> Mileage: {v[0]} kms, Fuel in the tank: {v[1]} lt.")