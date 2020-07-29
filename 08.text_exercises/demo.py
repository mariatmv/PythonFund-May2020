def get_letter_possition(letter):
    possition = 0
    if letter.isupper():
        possition = ord(letter) - 64
    else:
        possition = ord(letter) - 96
    return possition


def calculate_item_result(item):
    first_letter = item[0]
    last_letter = item[-1]
    number = int(item[1:-1])
    first_letter_possition = get_letter_possition(first_letter)
    last_letter_possition = get_letter_possition(last_letter)
    res = 0
    if first_letter.isupper():
        res = number / first_letter_possition
    else:
        res = number * first_letter_possition
    if last_letter.isupper():
        res -= last_letter_possition
    else:
        res += last_letter_possition
    return res


items = input().split()
total_sum = 0
for item in items:
    res = calculate_item_result(item)
    total_sum += res
print(f"{total_sum:.2f}")
