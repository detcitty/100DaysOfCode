# https://www.codewars.com/kata/545a4c5a61aa4c6916000755/train/python

'''
As a part of this Kata, you need to create a function that when provided 
with a triplet, returns the index of the numerical element that lies between the other two elements.

The input to the function will be an array of three distinct numbers 
(Haskell: a tuple).

For example:

gimme([2, 3, 1]) => 0

2 is the number that fits between 1 and 3 and the index of 2 in the 
input array is 0.

Another example (just to make sure it is clear):

gimme([5, 10, 14]) => 1

10 is the number that fits between 5 and 14 and the index of 10 in 
the input array is 1.
How do I use git in an efficient way?

'''
from itertools import combinations


def gimme(input_array):
    # Implement this function
    values = list(combinations(input_array, 2))
    
    # Insert a list comprehension
    list(map(lambda x: [True for i in x if i < 2], values))
    
    
