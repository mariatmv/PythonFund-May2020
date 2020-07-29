import math


def solve(a, b):
    first = math.factorial(a)
    second = math.factorial(b)
    res = first / second
    print(f"{res:.2f}")


first = int(input())
second = int(input())
solve(first, second)