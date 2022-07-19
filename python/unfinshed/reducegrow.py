# https://www.codewars.com/kata/57f780909f7e8e3183000078/train/python

'''
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

'''
import functools


def grow(arr):
    return(functools.reduce(lambda x, y: x*y, arr))
