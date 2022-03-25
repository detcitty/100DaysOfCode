# https://www.codewars.com/kata/554b4ac871d6813a03000035

def high_and_low(numbers):
    # ...
    text_numbers = numbers.split()
    int_numbers = list(map(lambda x : int(x), text_numbers))
    return("{} {}".format(max(int_numbers), min(int_numbers)))