budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
price_liter_milk = flour_price * 1.25
price_milk = price_liter_milk / 4
cozonacs_made = 0
colored_eggs = 0
price_cozonacs = flour_price + price_milk + eggs_price
while budget >= price_cozonacs:
    cozonacs_made += 1
    colored_eggs += 3
    if cozonacs_made % 3 == 0:
        colored_eggs -= cozonacs_made - 2
    budget -= price_cozonacs
print(f"You made {cozonacs_made} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")