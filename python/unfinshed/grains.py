# https://www.codewars.com/kata/55f7eb009e6614447b000099/train/python

from typing import Final


def square(number):
    #your code here
    final = 1
    for i in range(1,number):
        final *= 2
    return(final)
