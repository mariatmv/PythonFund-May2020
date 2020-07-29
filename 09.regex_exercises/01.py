import re
pattern = r'\d+'
text = ''
while True:
    sequence = input()
    if sequence == '':
        break
    text += sequence
numbers = re.findall(pattern, text)
print(' '.join(numbers))
