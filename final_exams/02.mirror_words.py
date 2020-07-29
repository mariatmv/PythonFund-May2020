import re
pattern = r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
mirror_words = []
string = input()
matches = re.findall(pattern, string, re.MULTILINE)
for match in matches:
    first_word = match[1]
    second_word = match[2]
    if first_word == second_word[::-1]:
        mirror_words.append(first_word + ' <=> ' + second_word)

if len(matches) == 0:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")

if len(mirror_words) == 0:
    print('No mirror words!')
else:
    print('The mirror words are:')
    print(', '.join(mirror_words))