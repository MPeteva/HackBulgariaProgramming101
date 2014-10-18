def is_int_palindrome(n):
    n = str(n)
    lenght = len(n)
    last = lenght//2

    for char in range(0, last):
        if not n[char] == n[lenght - char - 1]:
            return False

    return True


def main():
    num = int(input("Input a number: "))
    print (is_int_palindrome(num))


if __name__ == '__main__':
    main()
