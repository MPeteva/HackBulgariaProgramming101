def sevens_in_a_row(arr, n):
    br = 0
    for i in arr:
        if arr[i] == 7:
            #print (arr[i])
            br += 1
            #print (br)
        else:
            br == 0
        if br == n:
            return True
    return False


def main():
    array = list()
    num = int(input("Enter how many elements you want:"))
    print ('Enter numbers in array: ')
    for i in range(num):
        n = input()
        array.append(int(n))
    #print ('ARRAY: ', array)

    num_of_sevens = int(input("Enter number of sevens: "))
    print (sevens_in_a_row(array, num_of_sevens))


if __name__ == '__main__':
    main()
