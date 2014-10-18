def number_to_list(number):
    number_to_string = str(number)
    number_to_list = []

    for char in number_to_string:
        number_to_list.append(int(char))

    return number_to_list


def main():
    number = input("Input a number: ")
    print(number_to_list(number))


if __name__ == '__main__':
    main()
