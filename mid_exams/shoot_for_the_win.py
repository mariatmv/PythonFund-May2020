target_sequence = input().split()
command = input()
count = 0
while command != "End":
    index = int(command)
    current_value = None
    if 0 <= index <= len(target_sequence):
        for i in range(len(target_sequence)):
            if i == index:
                current_value = int(target_sequence.pop(i))
                target_sequence.insert(i, '-1')
                count += 1
                break
            else:
                current_value = 0
        for index, t in enumerate(target_sequence):
            if int(t) > -1:
                if int(t) > current_value:
                    res = int(t) - current_value
                    target_sequence[index] = str(res)
                else:
                    res = int(t) + current_value
                    target_sequence[index] = str(res)
    command = input()
print(f"Shot targets: {count} -> ", end='')
print(' '.join(target_sequence))