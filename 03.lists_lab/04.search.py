n = int(input())
word = input()
list = []
output = []
for i in range(n):
    string = input()
    list.append(string)
    if word in string:
        output.append(string)
print(list)
print(output)