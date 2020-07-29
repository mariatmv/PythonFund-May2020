import math
nums = list(map(int, input().split(', ')))
max_num = max(nums)
number_of_groups = math.ceil(max_num / 10)
for i in range(1, number_of_groups + 1):
    res = [num for num in nums if (i * 10) - 10 < num <= i * 10]
    print(f"Group of {i * 10}'s: {res}")