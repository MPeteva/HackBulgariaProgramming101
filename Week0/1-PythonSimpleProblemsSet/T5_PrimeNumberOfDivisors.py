from is_prime_4 import is_prime


def number_of_divisors(n):
    number = 0
    for i in range(1, n+1):
        if n % i == 0:
            number += 1
    return number


def prime_number_of_divisors(n):
    number_divisors = number_of_divisors(n)
    return is_prime(number_divisors)


def main():
    num = int(input("Input a number: "))
    print (prime_number_of_divisors(num))


if __name__ == '__main__':
    main()
