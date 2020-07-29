def get_percents(num):
    pattern = list()
    for i in range(num // 10):
        pattern.append("%")
    for i in range(10 - (num // 10)):
        pattern.append(".")
    print(f"{num}% [{''.join(map(str, pattern))}]")
    print("Still loading...")


loaded = int(input())
if loaded == 100:
    print("100% Complete!")
    print("[%%%%%%%%%%]")
else:
    get_percents(loaded)