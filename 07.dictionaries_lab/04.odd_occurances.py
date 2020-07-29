words = input().split()
dictionary = {}
for word in words:
    word = word.lower()
    if word not in dictionary:
        dictionary[word] = 0
    dictionary[word] += 1
for k, v in dictionary.items():
    if v % 2 != 0:
        print(k, end=" ")
