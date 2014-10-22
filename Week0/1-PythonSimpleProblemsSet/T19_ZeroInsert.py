def zero_insert(n):
    string = str(n)

    if len(string) == 1:
        return int(string)

    index = 1
    while index < len(string):
        if string[index-1] == string[index]:
            string = string[:index] + '0' + string[index:]
        if (int(string[index]) + int(string[index-1])) % 10 == 0:
            string = string[:index] + '0' + string[index:]
        index += 1

    return int(string)


def main():
    num = int(input("Input a number: "))
    print (zero_insert(num))


if __name__ == '__main__':
    main()
