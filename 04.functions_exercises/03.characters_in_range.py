first = input()
second = input()
first_in_acii = ord(first)
second_in_ascii = ord(second)


def get_symbols(a, b):
    for i in range(a + 1, b):
        print(chr(i), end=" ")


get_symbols(first_in_acii, second_in_ascii)
