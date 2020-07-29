quantity = int(input())
days = int(input())
ornament_price = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15
christmast_spirit = 0
day = 1
budget = 0
while day <= days:
    for day in range(1, days + 1):
        if day % 11 == 0:
            quantity += 2
        if day % 2 == 0:
            budget += ornament_price * quantity
            christmast_spirit += 5
        if day % 3 == 0:
            budget += (tree_skirt + tree_garlands) * quantity
            christmast_spirit += 13
        if day % 5 == 0:
            budget += tree_lights * quantity
            christmast_spirit += 17
        if day % 15 == 0:
            christmast_spirit += 30
        if day % 10 == 0:
            christmast_spirit -= 20
            budget += (tree_lights + tree_garlands + tree_skirt)
        day += 1
if days % 10 == 0:
    christmast_spirit -= 30
print(f"Total cost: {budget}")
print(f"Total spirit: {christmast_spirit}")