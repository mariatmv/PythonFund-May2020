from _collections import OrderedDict
n = int(input())
grades = {}
final = {}
for i in range(1, n + 1):
    name = input()
    grade = float(input())
    if name not in grades:
        grades[name] = [grade]
    else:
        grades[name].append(grade)
for k, v in grades.items():
    if sum(v) / len(v) >= 4.50:
        final[k] = sum(v) / len(v)
ordered = OrderedDict(sorted(final.items(), key=lambda x: x[1], reverse=True))
for k, v in ordered.items():
    print(f"{k} -> {v:.2f}")