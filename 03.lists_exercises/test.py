cards = input().split()
shuffles_count = int(input())
middle_index = len(cards) // 2
first_deck = []
second_deck = []
final_list = []
for card in range(0, middle_index):
    first_deck.append(cards[card])
for card in range(middle_index, len(cards)):
    second_deck.append(cards[card])
for card in range(len(cards)):
    for i in first_deck:
        final_list.append(i)
        for j in range(0, len(second_deck)):
            current_index = 1
            final_list[current_index].append(second_deck[j])
            current_index += 2
            break
        continue
print(final_list)