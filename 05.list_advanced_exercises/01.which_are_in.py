words = input().split(', ')
text = input()
res = [n for n in words if n in text]
print(res)