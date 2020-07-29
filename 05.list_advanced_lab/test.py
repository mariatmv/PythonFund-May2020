from statistics import mean
employees_happiness = [int(n) for n in input().split(' ')]
factor = int(input())
multiplied = [employee * factor for employee in employees_happiness]
filtered = list(filter(lambda n: n >= sum(multiplied) / len(multiplied), multiplied))
happy_ppl = len(filtered)
if happy_ppl >= len(multiplied) / 2:
    print(f"Score: {happy_ppl}/{len(multiplied)}. Employees are happy!")
else:
    print(f"Score: {happy_ppl}/{len(multiplied)}. Employees are not happy!")