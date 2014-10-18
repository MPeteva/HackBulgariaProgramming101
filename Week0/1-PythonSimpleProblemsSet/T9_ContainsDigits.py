from T8_ContainsDigit import contains_digit


def contains_digits(number, digits):
    for digit in digits:
        if not contains_digit(number, digit):
            return False

    return True


def main():
    number = input("Input a number: ")
    digits = input("Input a digits separated by comas and spaces: ")
    digits = digits.split(', ')

    print(contains_digits(number, digits))


if __name__ == '__main__':
    main()
