n = int(input())
list = []
filtered = []
for i in range(n):
    integer = int(input())
    list.append(integer)
command = input()
if command == "even":
    for i in list:
        if i % 2 == 0:
            filtered.append(i)
elif command == "odd":
    for i in list:
        if i % 2 != 0:
            filtered.append(i)
elif command == "positive":
    for i in list:
        if i >= 0:
            filtered.append(i)
elif command == "negative":
    for i in list:
        if i < 0:
            filtered.append(i)
print(filtered)