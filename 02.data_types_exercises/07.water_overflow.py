n = int(input())
poured = 0
for i in range(1, n + 1):
    pouring = int(input())
    poured += pouring
    if poured > 255:
        print("Insufficient capacity!")
        poured -=pouring
print(poured)