cards = input().split()
shuffles_count = int(input())
middle_index = len(cards) // 2
for i in range(shuffles_count):
    res = []
    for index in range(0, middle_index):
        first_card = cards[index]
        current_index = index + middle_index
        second_card = cards[current_index]
        res.append(first_card)
        res.append(second_card)
    cards = res
print(cards)