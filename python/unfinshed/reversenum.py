# https://www.codewars.com/kata/555bfd6f9f9f52680f0000c5/train/python

def reverse_number(n):
    math_abs = str(abs(n))
    str_reverse = (lambda x: list(math_abs)[x], list(range(len(math_abs)-1, -1, -1)))
    return(''.join(str_reverse))