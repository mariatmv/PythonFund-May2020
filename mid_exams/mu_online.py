health = 100
bitcoins = 0
is_success = True
rooms = input().split("|")
for room in range(0, len(rooms)):
    current_room = rooms[room].split(' ')
    command = current_room[0]
    value = int(current_room[1])
    if health <= 0:
        break
    if command == "potion":
        gained_health = 0
        if health + value <= 100:
            gained_health = value
            health += value
        else:
            gained_health = 100 - health
            health = 100
        print(f"You healed for {gained_health} hp.")
        print(f"Current health: {health} hp.")
    elif command == 'chest':
        bitcoins += value
        print(f"You found {value} bitcoins.")
    else:
        health -= value
        if health < 1:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room + 1}")
            is_success = False
        else:
            print(f"You slayed {command}.")
if is_success:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")