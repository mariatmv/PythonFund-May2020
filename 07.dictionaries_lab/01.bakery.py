elements = input().split()
res = {}
for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    res[key] = int(value)

print(res)