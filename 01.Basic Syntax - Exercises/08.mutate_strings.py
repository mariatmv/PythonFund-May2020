first = input()
second = input()
current = ''
for i in 0, len(first), +1:
    for j in 0, len(second), +1:
        current_new = first.replace(first[int(i)], second[int(j)], len(first))
        print(current)