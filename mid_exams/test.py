houses = list(map(int, input().split('@')))
command = input()
current_index = 0
while command != "Love!":
    tokens = command.split()
    lenght = int(tokens[1])
    current_index += lenght
    if current_index > len(houses) - 1:
        current_index = 0
    if houses[current_index] == 0:
        print(f"Place {current_index} already had Valentine's day.")
    else:
        houses[current_index] -= 2
        if houses[current_index] == 0:
            print(f"Place {current_index} has Valentine's day.")
    command = input()
print(f"Cupid's last position was {current_index}.")
if sum(houses) <= 0:
    print("Mission was successful.")
else:
    res = [count for count in range(len(houses)) if houses[count] > 0]
    print(f"Cupid has failed {len(res)} places.")