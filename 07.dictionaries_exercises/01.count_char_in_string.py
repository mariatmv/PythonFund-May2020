string = input()
s = string.replace(' ', '')
dictionary = {}
for i in s:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1
for k, v in dictionary.items():
    print(f"{k} -> {v}")