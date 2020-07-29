lost_fights = int(input())
expences = 0
shield_count = 0
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
for fight in range(1, lost_fights + 1):
    if fight % 2 == 0:
        expences += helmet_price
    if fight % 3 == 0:
        expences += sword_price
    if fight % 2 == 0 and fight % 3 == 0:
        expences += shield_price
        shield_count += 1
    if shield_count % 2 == 0 and shield_count >= 2:
        expences += armor_price
        shield_count = 0
print(f"Gladiator expenses: {expences:.2f} aureus")