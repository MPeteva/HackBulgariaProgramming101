def biggest_difference(arr):
    if len(arr) == 0:
        return False

    max_element = arr[0]
    min_element = arr[0]

    for element in arr:
        if max_element < element:
            max_element = element
        if min_element > element:
            min_element = element

    return min_element - max_element
