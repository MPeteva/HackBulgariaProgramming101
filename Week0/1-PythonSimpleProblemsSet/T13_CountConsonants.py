def count_consonants(str):
    CONSONANTS = "bcdfghjklmnpqrstvwxz"
    str = str.lower()
    number_of_consonants = 0

    for char in str:
        if char in CONSONANTS:
            number_of_consonants += 1

    return number_of_consonants

def main():
    Word = input("Input a word: ")
    print(count_consonants(Word))


if __name__ == '__main__':
    main()
