target_sequence = input().split()
command = input()
while command != "End":
    tokens = command.split()
    todo = tokens[0]
    index = int(tokens[1])
    if todo == "Shoot":
        power = int(tokens[2])
        if 0 <= index <= len(target_sequence):
            res = int(target_sequence[index]) - power
            target_sequence[index] = str(res)
            if int(target_sequence[index]) <= 0:
                target_sequence.pop(index)
    elif todo == "Add":
        value = tokens[2]
        if 0 <= index <= len(target_sequence):
            target_sequence.insert(index, value)
        else:
            print("Invalid placement!")
    elif todo == "Strike":
        radius = int(tokens[2])
        right_range = index + radius
        left_range = index - radius
        if 0 <= left_range and right_range <= len(target_sequence):
            for i in range(right_range, left_range - 1, -1):
                target_sequence.pop(i)
        else:
            print("Strike missed!")
    command = input()
print('|'.join(target_sequence))