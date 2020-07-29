words = input().split()
first = words[0]
second = words[1]
min_lenght = min(len(first), len(second))
total_sum = 0
for i in range(min_lenght):
    res = ord(first[i]) * ord(second[i])
    total_sum += res

biggest_word = first
if len(second) > len(first):
    biggest_word = second

for i in range(min_lenght, len(biggest_word)):
    total_sum += ord(biggest_word[i])

print(total_sum)