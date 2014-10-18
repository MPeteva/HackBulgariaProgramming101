from T4_IsPrime import is_prime


def number_of_divisors(n):
    number_of_divisors = 0

    for num in range(1, n+1):
        if n % num == 0:
            number_of_divisors += 1

    return number_of_divisors


def prime_number_of_divisors(n):
    if is_prime(n):
        return True

    number_divisors = number_of_divisors(n)
    return is_prime(number_divisors)


def main():
    num = int(input("Input a number: "))
    print (prime_number_of_divisors(num))


if __name__ == '__main__':
    main()
