groceries = input().split('!')
command = input()
while command != "Go Shopping!":
    tokens = command.split()
    todo = tokens[0]
    item = tokens[1]
    if todo == "Urgent":
        if item not in groceries:
            groceries.insert(0, item)
    elif todo == "Unnecessary":
        if item in groceries:
            groceries.remove(item)
    elif todo == "Correct":
        new_item = tokens[2]
        index = 0
        for i in groceries:
            if i == item:
                groceries[index] = new_item
            else:
                index += 1
    elif todo == "Rearrange":
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)

    command = input()
print(', '.join(groceries))