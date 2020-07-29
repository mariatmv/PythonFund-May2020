import sys
import math
count_of_students = int(input())
count_of_lectures = int(input())
initial_bonus = int(input())
max_bonus = -sys.maxsize
for student in range(1, count_of_students + 1):
    current_attendance = int(input())
    if current_attendance > max_bonus:
        max_bonus = current_attendance
bonus = max_bonus / count_of_lectures * (5 + initial_bonus)
print(f"Max Bonus: {math.ceil(bonus)}.")
print(f"The student has attended {max_bonus} lectures.")