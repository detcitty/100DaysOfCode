# https://www.codewars.com/kata/59f4a0acbee84576800000af/train/python
import numpy as np
import collections

def find_common_numbers(x):
    test1 = collections.Counter(x)
    return(test1)

def pos_average(s):
    # your code
    string_split = s.replace(" ", "").split(',')
    lists_of_lists = list(map(lambda x: list(x), string_split))
    numpy_array = np.array(lists_of_lists)
    int_array = numpy_array.astype(np.int16)
    vallues = np.apply_along_axis(find_common_numbers, 0, int_array)

    return(vallues)

test_str = "466960, 069060, 494940, 060069, 060090, 640009, 496464, 606900, 004000, 944096"
test1 = pos_average(test_str)
print(test1)