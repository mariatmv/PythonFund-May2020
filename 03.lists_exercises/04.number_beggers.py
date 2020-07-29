nums_str = input().split(", ")
beggers_count = int(input())
numbers = []
beggers = []
for num_str in nums_str:
    number = int(num_str)
    numbers.append(number)

for i in range(beggers_count):
    beggers.append(0)
index = 0
for number in numbers:
    beggers[index] += number
    index += 1
    if index == beggers_count:
        index = 0
print(beggers)