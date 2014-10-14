# def is_number_balanced(n):
#     middle = n//2 + 1
#     left_sum = 0
#     right_sum = 0
#     number_of_digits = 0

#     while n > 0:
#         number_of_digits += 1
#         n = n // 10

#     if number_of_digits % 2 == 1:
#         middle += 1
#     for i in range(number_of_digits, middle, -1):
#         right_sum += n % 10
#         n /= 10
#     for i in range(n//2, 0, -1):
#         left_sum += n % 10
#         n /= 10
#     if right_sum == left_sum:
#         return True
#     else:
#         return False


def is_number_balanced(number):
    middle = len(number) // 2
    left_side = number[:middle]

    if len(number) % 2 != 0:
        right_side = number[middle+1:]
    else:
        right_side = number[middle:]

    digit_sum = 0
    for char in left_side:
        digit_sum += int(char)

    for char in right_side:
        digit_sum -= int(char)

    return digit_sum == 0


def main():
    number = input("Input a number: ")
    print(is_number_balanced(number))


if __name__ == '__main__':
    main()
