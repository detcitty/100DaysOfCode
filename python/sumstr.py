# https://www.codewars.com/kata/5966e33c4e686b508700002d/train/python

def sum_str(a, b):
    # happy coding !
    int_a = 0 if not a else int(a)
    int_b = 0 if not b else int(b)

    return(str(sum([int_a, int_b])))
