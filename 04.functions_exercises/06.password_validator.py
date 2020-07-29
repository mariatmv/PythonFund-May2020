def validation(a):
    is_valid = True
    counter = 0
    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    for i in password:
        if i.isnumeric():
            counter += 1
    if counter < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        print("Password is valid")


password = input()
validation(password)