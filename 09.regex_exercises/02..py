import re
pattern = r'\b_[a-zA-Z0-9]+\b'
sequence = input()
variables = re.findall(pattern, sequence)
new = []
for v in variables:
    new.append(v[1:])
print(','.join(new))