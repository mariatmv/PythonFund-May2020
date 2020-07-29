needed_money = float(input())
months = int(input())
per_month = needed_money * 0.25
collected = 0
for i in range(1, months + 1):
    if i % 2 != 0 and i != 1:
        collected -= collected * 0.16
    if i % 4 == 0:
        collected += collected * 0.25
    collected += per_month
if collected >= needed_money:
    print(f"Bravo! You can go to Disneyland and you will have {(collected - needed_money):.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {(needed_money - collected):.2f}lv. more.")