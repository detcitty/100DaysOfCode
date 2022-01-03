# https://www.codewars.com/kata/54d496788776e49e6b00052f/train/python
import numpy as np

'''
Given an array of positive or negative integers

I= [i1,..,in]

you have to produce a sorted array P of the form

[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

P will be sorted by increasing order of the prime numbers. The final result has to be given as a string in Java, C#, C, C++ and as an array of arrays in other languages.
'''
def sum_for_list(lst):
    
    npl = np.array(lst)
    pass