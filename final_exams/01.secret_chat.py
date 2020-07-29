message = input()
command = input()
while command != "Reveal":
    command = command.split(':|:')
    todo = command[0]
    if todo == "InsertSpace":
        index = int(command[1])
        message = message[:index] + ' ' + message[index:]
        print(message)
    elif todo == "Reverse":
        substring = command[1]
        if substring in message:
            message = message.replace(substring, '', 1)
            message = message + substring[::-1]
            print(message)
        else:
            print('error')
    else:
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)
        print(message)
    command = input()
print(f"You have a new text message: {message}")