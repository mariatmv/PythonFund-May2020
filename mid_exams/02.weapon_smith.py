particles = input().split('|')
command = input()
while command != "Done":
    tokens = command.split()
    todo = tokens[0]
    if todo == "Move":
        direction = tokens[1]
        index = int(tokens[2])
        if direction == "Left":
            if 0 < index <= len(particles):
                part = particles.pop(index)
                particles.insert(index - 1, part)
        else:
            if 0 <= index < len(particles):
                part = particles.pop(index)
                particles.insert(index + 1, part)
    else:
        type = tokens[1]
        if type == "Even":
            res = [p for i, p in enumerate(particles) if i % 2 == 0]
            print(' '.join(res))
        else:
            res = [p for i, p in enumerate(particles) if i % 2 != 0]
            print(' '.join(res))
    command = input()
word = ''
for part in particles:
    word += part
print(f"You crafted {word}!")