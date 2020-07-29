from statistics import mean
sequence = list(map(int, input().split()))
average = mean(sequence)
sequence.sort(reverse=True)
greater = [sequence[i] for i in range(len(sequence)) if sequence[i] > average]
new_greater = []
for i, e in enumerate(greater):
    if i < 5:
        new_greater.append(e)
new = list(map(str, new_greater))
if sum(new_greater) > 0:
    print(' '.join(new))
else:
    print("No")