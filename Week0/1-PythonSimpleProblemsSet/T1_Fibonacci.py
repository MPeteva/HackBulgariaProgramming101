def nth_fibonacci(n):
    first = 1
    second = 1

    if n == 1 or n == 2:
        return first
    else:
        for i in range(n-2):
            new = first + second
            first = second
            second = new
        return new


def main():
    n = input("Enter a place in Fibonacci's row:")

    while not n.isdigit() or int(n) <= 0:
        print ("Sorry wrong input. Your place must be a positive number!")
        n = input("Please enter a new place in Fibonacci's row:")

    n = int(n)

    print (nth_fibonacci(n))


if __name__ == '__main__':
    main()
