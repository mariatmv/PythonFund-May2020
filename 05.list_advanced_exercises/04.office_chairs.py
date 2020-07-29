n = int(input())
total_free = 0
has_enough = True
for i in range(1, n + 1):
    room_data = input().split()
    chars_count = len(room_data[0])
    number_ppl = int(room_data[1])
    if chars_count >= number_ppl:
        total_free += chars_count - number_ppl
    else:
        has_enough = False
        print(f"{number_ppl - chars_count} more chairs needed in room {i}")
if has_enough:
    print(f"Game On, {total_free} free chairs left")