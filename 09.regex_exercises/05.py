import re
pattern = r'>>([a-zA-Z]+)<<(\d+(\.\d+)*)!(\d+)'
line = input()
spend = 0
print('Bought furniture:')
while line != "Purchase":
    match = re.fullmatch(pattern, line)
    if match is None:
        line = input()
        continue
    print(match[1])
    current = float(match[2]) * int(match[4])
    spend += current

    line = input()

print(f"Total money spend: {spend:.2f}")