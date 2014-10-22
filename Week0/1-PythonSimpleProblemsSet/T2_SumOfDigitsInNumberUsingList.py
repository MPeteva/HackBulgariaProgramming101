def sum_of_digits(n):
    if n < 0:
        n *= -1

    digits = []

    while n > 0:
        digits.append(n % 10)
        n = n // 10

    return sum(digits)
