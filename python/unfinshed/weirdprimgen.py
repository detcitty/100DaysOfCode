# https://www.codewars.com/kata/562b384167350ac93b00010c/train/python
import numpy as np
import sympy

'''
Consider the sequence a(1) = 7, a(n) = a(n-1) + gcd(n, a(n-1)) for n >= 2:

7, 8, 9, 10, 15, 18, 19, 20, 21, 22, 33, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 69, 72, 73....

Let us take the differences between successive elements of the sequence and get a second sequence g: 1, 1, 1, 5, 3, 1, 1, 1, 1, 11, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 23, 3, 1....

For the sake of uniformity of the lengths of sequences we add a 1 at the head of g:

g: 1, 1, 1, 1, 5, 3, 1, 1, 1, 1, 11, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 23, 3, 1...

Removing the 1s gives a third sequence: p: 5, 3, 11, 3, 23, 3... where you can see prime numbers.

'''
def count_ones(n):
    # your code
    # Help is one the way
    test = sympy.gcd(6, 8)
    pass

def max_pn(n):
    # your code
    pass

def an_over_average(n):
    # your code
    pass

