# https://www.codewars.com/kata/5ba38ba180824a86850000f7/train/python
import numpy as np

def solve(arr):
    np_return_arr = np.unique(arr, return_inverse=True)
    np_arr = np_return_arr[0]
    np_idx = np_return_arr[1]
    # Get the last value, similar to LIFO
    print(np_idx)
    print(np_return_arr)
    return(list(set(arr)))

test1 = solve([3,4,4,3,6,3])
print(test1)