def sum_of_divisors(n):
    if n == 0:
        return 0
#    if n == 1:
#        return 1

    sum = n           # Because every number is always dividing by itself

    for i in range(1, n//2 + 1):
        print (i)
        if n % i == 0:
            sum += i
    return sum


def main():
    num = int(input("Input a number: "))
    print (sum_of_divisors(num))


if __name__ == '__main__':
    main()
