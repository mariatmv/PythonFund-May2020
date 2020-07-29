array = list(map(int, input().split()))
command = input()
while command != "end":
    tokens = command.split()
    todo = tokens[0]
    if todo == "swap":
        first_index = int(tokens[1])
        second_index = int(tokens[2])
        first = ''
        second = ''
        for i in range(len(array)):
            if i == first_index:
                first = array[i]
                break
        for i in range(len(array)):
            if i == second_index:
                second = array[i]
                break
        array[first_index] = second
        array[second_index] = first
    elif todo == "multiply":
        first_index = int(tokens[1])
        second_index = int(tokens[2])
        old_first = array[first_index]
        first = array[second_index]
        second = old_first
        res = first * second
        array[first_index] = res
    else:
        for i in range(len(array)):
            current = array.pop(i)
            res = current - 1
            array.insert(i, res)
    command = input()
new_array = list(map(str, array))
print(', '.join(new_array))