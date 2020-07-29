list_of_gifts = input().split()
command = input().split()
while command[0] != "No":

    if command[0] == "OutOfStock":
        for gift in range(0, len(list_of_gifts)):
            if command[1] in list_of_gifts[gift]:
                list_of_gifts[gift] = "None"
    if command[0] == "Required":
        if int(command[2]) < len(list_of_gifts):
            list_of_gifts[int(command[2])] = command[1]
    if command[0] == "JustInCase":
        list_of_gifts[-1] = command[1]
    command = input().split()
for gift in range(0, len(list_of_gifts)):
    if "None" in list_of_gifts:
        list_of_gifts.remove("None")
print(" ".join(list_of_gifts))