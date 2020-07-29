data = input()
d = {}
while data != 'buy':
    data = data.split()
    name = data[0]
    price = float(data[1])
    quantity = int(data[2])
    if name not in d:
        d[name] = [price, quantity]
    else:
        d[name][0] = price
        d[name][1] += quantity
    data = input()
for k, v in d.items():
    print(f"{k} -> {(v[0] * v[1]):.2f}")