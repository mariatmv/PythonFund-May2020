def is_palindrome(text):
    counter = len(text) // 2
    is_palindrome = True
    for i in range(counter):
        second_index = len(text) - 1 - i
        if text[i] != text[second_index]:
            is_palindrome = False
            break
    return is_palindrome


def solve(items):
    for item in items:
        print(is_palindrome(item))


items = input().split(", ")
solve(items)


# def palindrome_checker(num_str):
#     return True if num_str == num_str[::-1] else False
#
#
# num_str_list = input().split(', ')
#
# for num_str in num_str_list:
#     print(palindrome_checker(num_str))