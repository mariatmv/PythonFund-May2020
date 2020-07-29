factor = int(input())
count = int(input())
found = 0
found_list = []
for i in range(1, 1000):
    if found < count:
        if i % factor == 0:
            found += 1
            found_list.append(i)
print(found_list)