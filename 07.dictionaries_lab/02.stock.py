elements = input().split()
searched = input().split()
products = {}
for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    products[key] = int(value)
for s in searched:
    if s in products:
        print(f"We have {products[s]} of {s} left")
    else:
        print(f"Sorry, we don't have {s}")