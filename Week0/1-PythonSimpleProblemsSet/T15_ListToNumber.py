def list_to_number(digits):
    list_to_string = ''

    for digit in digits:
        list_to_string += str(digit)

    if list_to_string == '':
        return False
    else:
        return int(list_to_string)
