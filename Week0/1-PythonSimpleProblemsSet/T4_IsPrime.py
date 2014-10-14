from math import sqrt, ceil


def is_prime(n):
    if n < 0:
        n = -1 * n
    is_number_prime = False if (n % 2 == 0 and n != 2 or n == 1) else True
    i = 3
    while i < (ceil(sqrt(n)) + 1) and is_number_prime:             # ceil - Round up sqrt(n) and we add 1 becouse we go through 2 numbers
        is_number_prime = (False if (n % i == 0) else True)
        i += 2
    return is_number_prime


def main():
    num = int(input("Input a number: "))
    print (is_prime(num))


if __name__ == '__main__':
    main()
