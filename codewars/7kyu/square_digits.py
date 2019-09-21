def square_digits(num):
    # use a string to build answer
    square_digits_string = ""

    # extract digits as per normal using the mod 10 approach, until num becomes 0
    while num > 0:
        least_significant_digit = num % 10
        # square digit and prepend it to string
        square_digits_string = "{}".format(
            least_significant_digit**2) + square_digits_string
        num //= 10

    # convert string to integer
    return int(square_digits_string)
