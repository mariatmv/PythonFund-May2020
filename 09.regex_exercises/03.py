import re
sentence = input().lower()
searched = input().lower()
pattern = searched
matched = re.findall(pattern, sentence)
print(len(matched))