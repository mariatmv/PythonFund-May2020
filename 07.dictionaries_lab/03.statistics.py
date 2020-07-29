products = input()
res = {}
while products != "statistics":
    products = products.split(': ')
    prod = products[0]
    quantity = int(products[1])
    if prod in res.keys():
        res[prod] += quantity
    else:
        res[prod] = quantity
    products = input()
print("Products in stock:")
for k, v in res.items():
    print(f"- {k}: {v}")
print(f"Total Products: {len(res.keys())}")
print(f"Total Quantity: {sum(res.values())}")