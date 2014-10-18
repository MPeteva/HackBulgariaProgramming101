def count_vowels(string):
    VOWELS = "aeiouy"
    string_for_counting_vowels = string.lower()
    number_of_vowels = 0

    for char in string_for_counting_vowels:
        if char in VOWELS:
            number_of_vowels += 1

    return number_of_vowels


def main():
    string = input("Input a string: ")
    print(count_vowels(string))


if __name__ == '__main__':
    main()
