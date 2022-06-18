# https://www.codewars.com/kata/54d81488b981293527000c8f/train/python
'''
Sum of Pairs
Given a list of integers and a single sum value, 
return the first two values (parse from the left please) 
in order of appearance that add up to form the sum.
'''
#import numpy as np
import statistics
def sum_pairs(ints, s):
    mean_ints = statistics.mean(ints)
    median_ints = statistics.median(ints)
    mode_ints = statistics.mode(ints)
    half_ints = [x / 2.0 for x in ints]
    return