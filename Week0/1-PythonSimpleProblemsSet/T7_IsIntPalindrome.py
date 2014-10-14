def is_int_palindrome(n):
    last = n//2
    for i in range(0, last):
        if n[i] != n[last - i]:
            return False
    return True


def main():
    num = int(input("Input a number: "))
    print (is_int_palindrome(num))


if __name__ == '__main__':
    main()
