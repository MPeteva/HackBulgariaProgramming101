def list_to_number(digits):
    list_to_string = ''

    for char in digits:
#       if char.isdigit():
        list_to_string += str(char)

    if list_to_string == '':
        return False
    else:
        return int(list_to_string)

# Raboti samo ot testovete zashtoto ne znam kak da vuveda list ot ekrana.....?????
#def main():
#    numbers = input("Input numbers: ")
#    list_of_numbers = list(numbers)

#    list_of_numbers = input("Input a list of numbers: ")
#    print(list_to_number(list_of_numbers))


#if __name__ == '__main__':
#    main()
