def sum_of_divisors(n):
    sum = 0
    for i in range(1, n+1):
        if n % i == 0:
            sum += i
    return sum


def main():
    num = int(input("Input a number: "))
    print (sum_of_divisors(num))


if __name__ == '__main__':
    main()
