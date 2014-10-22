def sum_of_digits(n):
    if n < 0:
        n *= -1

    sum = 0

    while (n > 0):
        sum += n % 10
        n //= 10           # integer division
    return sum


def main():
    num = int(input("Input a number: "))
    print (sum_of_digits(num))


if __name__ == '__main__':
    main()
