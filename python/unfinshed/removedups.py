# https://www.codewars.com/kata/5ba38ba180824a86850000f7/train/python
import numpy as np

def solve(arr):
    print(np.unique(arr, return_index=True))
    return(list(set(arr)))

test1 = solve([3,4,4,3,6,3])
print(test1)