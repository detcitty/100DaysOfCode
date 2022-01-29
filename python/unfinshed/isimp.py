# https://www.codewars.com/kata/556b85b433fb5e899200003f/train/python
import re
imprt numpy as np

def mixed_fraction(s):
    num, denom = split("/")
    whole_ = int(int(num) / int(denom))
    remainder_ = int(num) % int(denom))
    test = np.array(whole_ / remainder)
    return(test)
