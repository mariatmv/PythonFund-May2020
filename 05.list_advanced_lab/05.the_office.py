happiness_indexes = [int(n) for n in input().split(' ')]
improvement_factor = int(input())
factored_happiness = [v * improvement_factor for v in happiness_indexes]
average_happiness = sum(factored_happiness) / len(factored_happiness)
happy_values = list(filter(lambda n: n >= average_happiness, factored_happiness))
happy_count = len(happy_values)
if happy_count >= (len(happiness_indexes) / 2):
    print(f"Score: {happy_count}/{len(happiness_indexes)}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{len(happiness_indexes)}. Employees are not happy!")