d = {}
resourse = input()
while resourse != "stop":
    quantity = int(input())
    if resourse in d:
        d[resourse] += quantity
    else:
        d[resourse] = quantity
    resourse = input()
for k, v in d.items():
    print(f"{k} -> {v}")