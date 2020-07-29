n = int(input())
taken = {}
for i in range(1, n + 1):
    command = input().split()
    todo = command[0]
    username = command[1]
    if todo == "register":
        lisence_plate = command[2]
        if username not in taken:
            taken[username] = lisence_plate
            print(f"{username} registered {lisence_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {taken[username]}")
    else:
        if username not in taken:
            print(f"ERROR: user {username} not found")
        else:
            del taken[username]
            print(f"{username} unregistered successfully")
for k, v in taken.items():
    print(f"{k} => {v}")