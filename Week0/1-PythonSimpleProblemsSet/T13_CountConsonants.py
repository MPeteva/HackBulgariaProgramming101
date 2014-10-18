def count_consonants(string):
    CONSONANTS = "bcdfghjklmnpqrstvwxz"
    string_for_counting_consonants = string.lower()
    number_of_consonants = 0

    for char in string_for_counting_consonants:
        if char in CONSONANTS:
            number_of_consonants += 1

    return number_of_consonants


def main():
    string = input("Input a string: ")
    print(count_consonants(string))


if __name__ == '__main__':
    main()
