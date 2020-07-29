import math
people = int(input())
capacity = int(input())
full_courses = math.floor(people / capacity)
if people % full_courses == 0:
    print(full_courses)
else:
    print(full_courses + 1)
