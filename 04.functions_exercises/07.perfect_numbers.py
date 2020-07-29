def is_number_perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num


number = int(input())
if is_number_perfect(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")