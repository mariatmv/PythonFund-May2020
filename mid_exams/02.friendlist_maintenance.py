friends_usernames = input().split(', ')
command = input()
blacklisted = 0
lost = 0
while command != "Report":
    tokens = command.split()
    todo = tokens[0]
    if todo == "Blacklist":
        name = tokens[1]
        if name not in friends_usernames:
            print(f"{name} was not found.")
        else:
            for i, n in enumerate(friends_usernames):
                if n == name:
                    friends_usernames[i] = "Blacklisted"
                    print(f"{name} was blacklisted.")
                    blacklisted += 1
    elif todo == "Error":
        index = int(tokens[1])
        if friends_usernames[index] != "Blacklisted" and friends_usernames[index] != "Lost":
            name = friends_usernames[index]
            friends_usernames[index] = "Lost"
            print(f"{name} was lost due to an error.")
            lost += 1
    else:
        index = int(tokens[1])
        new_name = tokens[2]
        if 0 <= index <= len(friends_usernames):
            old_name = friends_usernames[index]
            friends_usernames[index] = new_name
            print(f"{old_name} changed his username to {new_name}.")
    command = input()
print(f"Blacklisted names: {blacklisted}")
print(f"Lost names: {lost}")
print(' '.join(friends_usernames))