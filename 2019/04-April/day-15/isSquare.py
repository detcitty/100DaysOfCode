# https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python

import math

def is_square(n):
    sqrt = 0
    if (n < 0):
        return False
    elif(n == 0):
        return True

    else:

        sqrt = math.sqrt(n)
        if (sqrt % 1 == 0):
            return True

    return False # fix me
