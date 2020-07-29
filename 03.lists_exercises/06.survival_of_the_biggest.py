input_data = input().split()
to_be_removed = int(input())
removed = 0
smallest = 8932948234
while removed < to_be_removed:
    for i in input_data:
        if int(i) < smallest:
            smallest = int(i)
    input_data.remove(str(smallest))
    removed += 1
    smallest = 3828943289
print("[", end="")
print(", ".join(input_data), end="")
print("]")