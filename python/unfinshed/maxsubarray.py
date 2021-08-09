# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python
import numpy as np
from itertools import combinations

def max_sequence(arr):
    index_values_tuples = list(combinations(range(len(arr)+1), 2))
    index_values = list(map(lambda x: slice(x[0], x[1]), index_values_tuples))
    # print(index_values)
    found_sums = []
    for i, e in enumerate(index_values):
        sub_array = arr[e]
        found_sums.append(sum(sub_array))
    
    is_empty = True if len(arr) == 0 else False

    return(max(found_sums) if not is_empty and max(arr) >= 0 else 0)

test1 = max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(test1)