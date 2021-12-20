'''
Problem 4
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

999*999 = 998001
999*998 = 997002
'''

import numpy as np
import math

def find_palindrome(np_value):
    num_str = str(np_value)
    len_str = len(num_str)
    num_array = list(num_str)

    for i in range(len_str):
        i
    

test_values = np.array(list(range(900, 999)))
print(test_values * 997)