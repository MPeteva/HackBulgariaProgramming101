def sevens_in_a_row(arr, n):
    if len(arr) == 0:   # if the array is empty
        if n == 0:
            return True
        else:
            return False

    Number_of_serial_sevens = 0

    for number in range(0, len(arr)):
        if arr[number] == 7:   # if we found seven we count it
            Number_of_serial_sevens += 1
        else:                # if not we must check if the series is long enogh
            if Number_of_serial_sevens == n:
                return True
            Number_of_serial_sevens = 0

    if Number_of_serial_sevens == n:
            return True

    return False


def main():
    array = list()
    num = int(input("Enter how many elements you want:"))
    print ('Enter numbers in array: ')
    for i in range(num):
        n = input()
        array.append(int(n))

    num_of_sevens = int(input("Enter number of sevens: "))
    print (sevens_in_a_row(array, num_of_sevens))


if __name__ == '__main__':
    main()
