def contains_digit(number, digit):
    string = str(number)
    char = str(digit)
    if char in string:
        return True
    return False


def main():
    num = int(input("Input a number: "))
    digit = int(input("Input a digit to check if the number contains it: "))
    print (contains_digit(num, digit))


if __name__ == '__main__':
    main()
