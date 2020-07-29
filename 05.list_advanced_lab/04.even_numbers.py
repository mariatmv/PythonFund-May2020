numbers = map(int, input().split(', '))
print([i for i, n in enumerate(numbers) if n % 2 == 0])