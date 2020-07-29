a = int(input())
b = int(input())
greatest = 0
for i in range(1, b + 1):
    if i % a == 0 and i <= b:
        greatest = i
print(greatest)