targets = list(map(int, input().split('|')))
command = input()
points = 0
while command != "Game over":
    tokens = command.split()
    todo = tokens[0]
    if todo == "Shoot":
        cordinates = tokens[1].split('@')
        direction = cordinates[0]
        start_index = int(cordinates[1])
        lenght = int(cordinates[2])
        if direction == "Right":
            if 0 <= start_index < len(targets):
                if start_index + lenght > 0:
                    current_index = (start_index + lenght) % len(targets)
                else:
                    current_index = start_index + lenght
                if targets[current_index] >= 5:
                    targets[current_index] -= 5
                    points += 5
                elif 0 < targets[current_index] < 5:
                    points += targets[current_index]
                    targets[current_index] = 0
        else:
            if 0 <= start_index < len(targets):
                if start_index - lenght < 0:
                    current_index = (start_index - lenght) % len(targets)
                else:
                    current_index = start_index - lenght
                if targets[current_index] >= 5:
                    targets[current_index] -= 5
                    points += 5
                elif 0 < targets[current_index] < 5:
                    points += targets[current_index]
                    targets[current_index] = 0
    elif todo == "Reverse":
        targets.reverse()
    command = input()
res = []
for target in targets:
    res.append(str(target))
print(' - '.join(res))
print(f"Iskren finished the archery tournament with {points} points!")