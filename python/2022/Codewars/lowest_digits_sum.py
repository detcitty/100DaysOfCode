# https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python
import numpy as np

def sum_two_smallest_numbers(numbers):
    #your code here
    a = np.array(numbers)
    sort_a = np.sort(a)
    sum_ = sort_a[0] + sort_a[1]
    return(sum_)