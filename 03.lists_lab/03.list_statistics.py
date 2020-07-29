n = int(input())
possitives = []
negatives = []
count = 0
sum = 0
for i in range(n):
    current = int(input())
    if current >= 0:
        possitives.append(current)
        count += 1
    else:
        negatives.append(current)
        sum += current
print(possitives)
print(negatives)
print(f"Count of positives: {count}. Sum of negatives: {sum}")