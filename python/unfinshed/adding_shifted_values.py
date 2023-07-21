# https://www.codewars.com/kata/57c7231c484cf9e6ac000090/train/python

'''
#Adding values of arrays in a shifted way

You have to write a method, that gets two parameter:

1. An array of arrays with int-numbers
2. The shifting value
#The method should add the values of the arrays to one new array.

The arrays in the array will all have the same size and this size will always be greater than 0.
The shifting value is always a value from 0 up to the size of the arrays.
There are always arrays in the array, so you do not need to check for null or empty.

#1. Example:

[[1,2,3,4,5,6], [7,7,7,7,7,-7]], 0

1,2,3,4,5,6
7,7,7,7,7,-7

--> [8,9,10,11,12,-1]
#2. Example

[[1,2,3,4,5,6], [7,7,7,7,7,7]], 3

1,2,3,4,5,6
      7,7,7,7,7,7

--> [1,2,3,11,12,13,7,7,7]
#3. Example

[[1,2,3,4,5,6], [7,7,7,-7,7,7], [1,1,1,1,1,1]], 3


1,2,3,4,5,6
      7,7,7,-7,7,7
            1,1,1,1,1,1

--> [1,2,3,11,12,13,-6,8,8,1,1,1]
Have fun coding it and please don't forget to vote and rank this kata! :-)

I have created other katas. Have a look if you like coding and challenges.
'''

import numpy as np

def sum_arrays(arrays, shift):
    shifted_lists = []
    level = 1

    for lst in arrays:
        num_leading_zeros = level * shift
        zeros = num_leading_zeros * [0]

        # 0 * [0] is an empty array
        combinded_array = zeros + lst
    
    max_length = max(map(lambda x: len(x), shifted_lists))

    final_arrays = []
    for lst in shifted_lists:
        diff_size = max_length - len(lst)
        preceeding_zeros = diff_size * [0]
        final_arrays.append(lst + preceeding_zeros)

    return(final_arrays)
    

    