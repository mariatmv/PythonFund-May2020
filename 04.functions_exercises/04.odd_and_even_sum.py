def odd_sum(num):
    suma = 0
    for i in num:
        if i % 2 != 0:
            suma += i
    return suma


def even_sum(num):
    suma = 0
    for i in num:
        if i % 2 == 0:
            suma += i
    return suma


number = input()
numbers = [int(x) for x in str(number)]
odd = odd_sum(numbers)
even = even_sum(numbers)
print(f"Odd sum = {odd}, Even sum = {even}")
