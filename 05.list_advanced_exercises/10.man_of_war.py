def is_valid_index(len, index):
    return 0 <= index < len


pirate_ship = list(map(int, input().split('>')))
war_ship = list(map(int, input().split('>')))
lenght_warship = len(war_ship)
lenght_pirateship = len(pirate_ship)
max_health_capacity = int(input())
command_input = input()
while command_input != "Retire":
    tokens = command_input.split()
    command = tokens[0]
    if command == "Fire":
        index = int(tokens[1])
        damage = int(tokens[2])
        if not is_valid_index(lenght_warship, index):
            command_input = input()
            continue
        war_ship[index] -= damage
        if war_ship[index] <= 0:
            print("You won! The enemy ship has sunken.")
            break
        command_input = input()
    elif command == "Defend":
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        damage = int(tokens[3])
        if not is_valid_index(lenght_pirateship, start_index):
            command_input = input()
            continue
        if not is_valid_index(lenght_pirateship, end_index):
            command_input = input()
            continue
        for section in range(pirate_ship[start_index], pirate_ship[end_index]):
            section -= damage
            if section <= 0:
                print("You lost! The pirate ship has sunken.")
                break
    elif command == "Repair":
        pass