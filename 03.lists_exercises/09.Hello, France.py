from typing import List

items = input().split("|")
budget = float(input())
is_valid = False
profit = 0.00
sum = 0
sold = []
for item in range(0, len(items)):
    current_item = items[item].split("->")
    item_type = current_item[0]
    price = current_item[1]
    if item_type == "Clothes" and float(price) <= 50.00 and budget >= float(price):
        budget -= float(price)
        current_profit = round(float(price) + (float(price) * 0.40), 2)
        sum += current_profit
        profit += current_profit - float(price)
        sold.append(str(current_profit))
    elif item_type == "Shoes" and float(price) <= 35.00 and budget >= float(price):
        budget -= float(price)
        current_profit = round(float(price) + (float(price) * 0.40), 2)
        sum += current_profit
        profit += current_profit - float(price)
        sold.append(str(current_profit))
    elif item_type == "Accessories" and float(price) <= 20.50 and budget >= float(price):
        budget -= float(price)
        current_profit = round(float(price) + (float(price) * 0.40), 2)
        sum += current_profit
        sold.append(str(current_profit))
        profit += current_profit - float(price)
print(" ".join(sold))
print(f""
      f"Profit: {profit:.2f}")
if budget + sum >= 150:
    print("Hello, France!")
else:
    print("Time to go.")