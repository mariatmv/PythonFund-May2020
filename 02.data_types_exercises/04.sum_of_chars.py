n = int(input())
sum = 0
for i in range(1, n + 1):
    letter = input()
    sum += ord(letter)
print(f"The sum equals: {sum}")