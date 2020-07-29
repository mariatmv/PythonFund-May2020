number = int(input())
current = number
while True:
    year = str(number)
    if len(set(year)) == len(year):
        current = year
        break
    if current != number:
        print(current)
    number += 1