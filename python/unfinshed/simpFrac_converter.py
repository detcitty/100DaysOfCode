# https://www.codewars.com/kata/556b85b433fb5e899200003f/train/python

'''



Given a string representing a simple fraction x/y, your function must return a string representing the corresponding mixed fraction in the following format:

[sign]a b/c

where a is integer part and b/c is irreducible proper fraction. There must be exactly one space between a and b/c. Provide [sign] only if negative (and non zero) and only at the beginning of the number (both integer part and fractional part must be provided absolute).

If the x/y equals the integer part, return integer part only. If integer part is zero, return the irreducible proper fraction only. In both of these cases, the resulting string must not contain any spaces.

Division by zero should raise an error (preferably, the standard zero division error of your language).
Value ranges

    -10 000 000 < x < 10 000 000
    -10 000 000 < y < 10 000 000


'''

def mixed_fraction(s):
    return None