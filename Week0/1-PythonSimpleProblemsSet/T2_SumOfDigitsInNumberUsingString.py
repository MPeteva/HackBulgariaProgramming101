def sum_of_digits(n):
    sum = 0

    if n < 0:
        n = -1 * n

    n = str(n)

    for digit in n:         # Deviding a sting into characters
        sum += int(digit)

    return sum


def main():
    num = int(input("Input a number: "))

    print (sum_of_digits(num))


if __name__ == '__main__':
    main()
