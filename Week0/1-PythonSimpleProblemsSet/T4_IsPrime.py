from math import sqrt, ceil


def is_prime(n):
    if n <= 1:
        return False

    if n % 2 == 0 and not n == 2:
        return False

    for i in range(3, ceil(sqrt(n)) + 1, 2):  # ceil-Round UP flour number
                                            # +1 because we go through 2 steps
        if n % i == 0:
            return False

    return True

def main():
    num = int(input("Input a number: "))
    print (is_prime(num))


if __name__ == '__main__':
    main()
