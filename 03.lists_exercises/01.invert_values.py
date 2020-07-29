string = input()
list = string.split()
inverted = []
for i in list:
    inverted.append(int(i) * -1)
print(inverted)