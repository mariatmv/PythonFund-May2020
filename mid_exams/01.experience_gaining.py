needed_experience = int(input())
count_of_battles = int(input())
collected_experience = 0
is_success = False
count = 0
for i in range(1, count_of_battles + 1):
    bonus = 0
    if collected_experience >= needed_experience:
        is_success = True
        break
    current_battle = int(input())
    if i % 3 == 0 and i:
        bonus = current_battle * 0.15
    if i % 5 == 0:
        bonus -= current_battle * 0.10
    collected_experience += current_battle + bonus
    count += 1
if collected_experience >= needed_experience:
    is_success = True
if is_success:
    print(f"Player successfully collected his needed experience for {count} battles.")
else:
    print(f"Player was not able to collect the needed experience, {(needed_experience - collected_experience):.2f} more needed.")