def count_substrings(haystack, needle):
    count_of_occurrences = haystack.count(needle)
    return count_of_occurrences


def main():
    String = input("Input a string: ")
    Word = input("Input a word to count occurrences of it in string: ")
    print (count_substrings(String, Word))


if __name__ == '__main__':
    main()
