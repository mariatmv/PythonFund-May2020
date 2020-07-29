from _collections import OrderedDict
import operator
command = input()
courses = dict()
while command != "end":
    command = command.split(' : ')
    course = command[0]
    student = command[1]
    if course not in courses:
        courses[course] = [student]
    else:
        courses[course].append(student)
    command = input()
ordered = OrderedDict(sorted(courses.items(), key=lambda c: len(c[1]), reverse=True))
for k, v in ordered.items():
    print(f"{k}: {len(v)}")
    for value in sorted(v):
        print(f"-- {value}")