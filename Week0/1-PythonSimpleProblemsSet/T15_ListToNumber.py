def list_to_number(digits):
    list_to_string = ''

    for char in digits:
#       if char.isdigit():
        list_to_string += str(char)

    if list_to_string == '':
        return False
    else:
        return int(list_to_string)
