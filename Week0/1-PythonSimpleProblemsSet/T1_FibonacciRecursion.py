def nth_fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return nth_fibonacci(n-1) + nth_fibonacci(n-2)


def main():
    n = input("Enter a place in Fibonacci's row:")

    while not n.isdigit() or int(n) <= 0:               # Is the input corect
        print ("Sorry wrong input. Your place must be a positive number!")
        n = input("Please enter a new place in Fibonacci's row:")

    n = int(n)

    print (nth_fibonacci(n))


if __name__ == '__main__':
    main()
