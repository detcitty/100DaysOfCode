# https://www.codewars.com/kata/58fea5baf3dff03a6e000102/train/python
import math
def factor_digit(n):
    list_factors = list(range(1,n+1))
    magic_number = math.prod(list_factors)
    list_magicNumbers = list(str(magic_number))
    return(len(list_magicNumbers))