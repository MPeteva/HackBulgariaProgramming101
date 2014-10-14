def count_vowels(str): # kakva beshe funkciqta dali edin string e chast ot drug string
    VOWERS = "aeiouy"
    str = str.lower()
    number_of_vowels = 0

    for char in str:
        if char in VOWERS:
            number_of_vowels += 1

    return number_of_vowels


def main():
    Word = input("Input a word: ")
    print(count_vowels(Word))


if __name__ == '__main__':
    main()
