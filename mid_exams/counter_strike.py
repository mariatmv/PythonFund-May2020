initual_energy = int(input())
distance = input()
won_games = 0
is_success = True
while distance != "End of battle":
    distance = int(distance)
    if distance > initual_energy:
        is_success = False
        print(f"Not enough energy! Game ends with {won_games} won battles and {initual_energy} energy")
        break
    won_games += 1
    initual_energy -= distance
    if won_games % 3 == 0:
        initual_energy += won_games
    distance = input()

if is_success:
    print(f"Won battles: {won_games}. Energy left: {initual_energy}")