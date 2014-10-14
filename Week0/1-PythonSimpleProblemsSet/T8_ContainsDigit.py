def contains_digit(number, digit):
    while (number > 0):
        if number % 10 == digit:
            return True
        number = number // 10
    return False


def main():
    num = int(input("Input a number: "))
    digit = int(input("Input a digit to check if the number contains it: "))
    print contains_digit(num, digit)


if __name__ == '__main__':
    main()
