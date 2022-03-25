# https://www.codewars.com/kata/5748838ce2fab90b86001b1a/train/python
import math

def square_area(A):
    # your code here
    # circum = 2 * math.pi * r
    # # circum = 4 * arc
    # arc = circum / 4
    # 2 * math.pi * r = 4 * arc
    r = (4 * A)  / (2 * math.pi)

    return(round(r**2, 2))