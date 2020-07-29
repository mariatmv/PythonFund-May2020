count = int(input())
synonims = {}
for i in range(count):
    word = input()
    synonim = input()
    if word not in synonims:
        synonims[word] = []
    synonims[word].append(synonim)
for word in synonims:
    print(f"{word} - {', '.join(synonims[word])}")