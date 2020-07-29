usernames = input().split(', ')
valid = []
isValid = False
for name in usernames:
    if 3 <= len(name) <= 16:
        isValid = True
        for ch in name:
            if ch.isalnum() or ord(ch) == 95 or ord(ch) == 45:
                isValid = True
            else:
                isValid = False
                break
    if isValid:
        valid.append(name)
    isValid = False


print('\n'.join(valid))