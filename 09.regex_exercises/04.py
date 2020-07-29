import re
text = input()
user_pattern = r'[a-zA-Z0-9]+((\.|\-|\_)?[a-zA-Z0-9]+)*'
host_pattern = r'[a-zA-z]+(-[a-zA-Z]+)*(\.[a-zA-z]+(-[a-zA-Z]+)*)+'
pattern = rf"{user_pattern}@{host_pattern}"
matches = re.finditer(pattern, text)
for m in matches:
    print(m[0])