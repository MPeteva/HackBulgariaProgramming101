from contains_digit_8 import contains_digit

# def contains_digits(number, digits):
#     number_of_contained = 0
#     number_digits # number of elements in list digits
#     for i in range(number_digits):
#         if contains_digits(number, digits[i]):
#             number_of_contained += 1
#     if number_digits == number_of_contained:
#         return True
#     else:
#         return False


def contains_digits2(number, digits):
    number = str(number)
    for digit in digits:
        if not contains_digit(number, digit):
            return False

    return True


def main():
    number = input("Input a number: ")
    digits = input("Input a digits: ")
    digits = digits.split(', ')

    print(contains_digits2(number, digits))


if __name__ == '__main__':
    main()
