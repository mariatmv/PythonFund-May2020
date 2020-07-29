collecting_items = input().split(', ')
command = input().split(' - ')
while command[0] != "Craft!":
    current_command = command[0]
    item = command[1]
    if current_command == 'Collect':
        if item in collecting_items:
            pass
        else:
            collecting_items.append(item)
    elif current_command == 'Drop':
        if item in collecting_items:
            collecting_items.remove(item)
    elif current_command == 'Combine Items':
        items = command[1].split(':')
        old = items[0]
        new = items[1]
        for item in collecting_items:
            if item == old:
                index_of_old = collecting_items.index(old)
                collecting_items.insert(index_of_old + 1, new)
    elif current_command == 'Renew':
        if item in collecting_items:
            collecting_items.remove(item)
            collecting_items.append(item)

    command = input().split(' - ')
print(', '.join(collecting_items))