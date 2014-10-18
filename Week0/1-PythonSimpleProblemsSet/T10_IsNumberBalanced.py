def is_number_balanced(number):
    number = str(number)
    lenght = len(number)
    last = lenght // 2

    sum_left = 0
    sum_right = 0

    for char in range(0, last):
        sum_left += int(number[char])
        sum_right += int(number[lenght - char - 1])

    return True if sum_left == sum_right else False



#def is_number_balanced1(number):
#    middle = len(number) // 2
#    left_side = number[:middle] !!!
#
#    if len(number) % 2 != 0:
#        right_side = number[middle+1:] !!!
#    else:
#        right_side = number[middle:] !!!
#
#    digit_sum = 0
#    for char in left_side:
#        digit_sum += int(char)
#
#    for char in right_side:
#        digit_sum -= int(char)
#
#    return digit_sum == 0


def main():
    number = input("Input a number: ")
    print(is_number_balanced(number))


if __name__ == '__main__':
    main()
